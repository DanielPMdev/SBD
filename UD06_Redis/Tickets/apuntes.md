Buena — vamos a hacerlo práctico y directo. Te propongo una arquitectura Redis simple y segura que cumple tus requisitos (usar Redis como almacenamiento, evitar doble-login simultáneo, “cuando un usuario hace login se almacena”, usar **dos estructuras de datos distintas además de un índice**). Luego te doy los comandos Redis exactos y la lógica por endpoint.

# Resumen de diseño (decisiones)

* **Estructuras Redis usadas:**

  1. **SET** (conjunto) → para controlar usuarios conectados (evita doble-login con operaciones atómicas).
  2. **HASH** → para almacenar datos del *session* y para almacenar los datos del *ticket* (detallados por id).
  3. **JSON con INDEX** → *índice* para listar tickets por usuario.

(Eso son 2 estructuras distintas — SET y HASH — **más** un índice ZSET.)

# Esquema de claves y tipos

* `connected_users` → **SET**
  Contiene los user IDs actualmente logueados. (SADD/SREM para añadir/quitar)
* `session:{user}` → **HASH**
  Campos: `sid`, `login_at`, `ip`, `meta…`
* `ticket:{ticketId}` → **HASH**
  Campos: `id`, `user`, `created_at`, `evento`, `seat`, `price`, ...
* `user:{user}:tickets` → **ZSET** (índice por timestamp)
  Score = timestamp (epoch ms), member = ticketId
  Permite listar tickets por usuario ordenados por fecha.

(Opcional: `tickets_seq` **INCR** para generar ids incrementales, o usa UUID en la app.)

# Lógica por endpoint (comandos + atomicidad)

### 1) `POST /user/login`

Objetivo: crear sesión solo si no existe sesión activa para el usuario.

Flujo seguro y atómico (usando SADD para evitar race conditions):

1. Generar `sid` (UUID) en la aplicación.

2. Intentar añadir usuario al set:

   ```
   SADD connected_users <user>
   ```

   * Si devuelve `1` → no existía, continuar.
   * Si devuelve `0` → ya estaba conectado → devolver error “already logged in”.

3. Si SADD devolvió 1, crear hash de sesión:

   ```
   HMSET session:<user> sid <sid> login_at <ts> ip <ip> meta <json>
   ```

   (También puedes usar `HSET` por campo).

4. (Opcional) establecer TTL en la sesión si quieres tiempo máximo:

   ```
   EXPIRE session:<user> 3600
   ```

En pseudo-código (Node/Node-RED):

```js
const added = await redis.sadd("connected_users", user);
if (added === 0) return 409; // usuario ya conectado
await redis.hset(`session:${user}`, { sid, login_at: Date.now(), ip });
return { sid };
```

> Alternativa atómica con Lua: si quieres crear `session:{user}` y añadir al set en 1 paso atómico, puedes hacerlo en un script Lua. Pero SADD + HSET es suficiente en la mayoría de casos porque SADD es atómico y si SADD falla no haces HSET.

---

### 2) `POST /ticket/buy`

Objetivo: crear ticket y asociarlo al usuario (indexar para búsquedas).

Flujo:

1. Generar `ticketId` (INCR `tickets_seq` o UUID).

   ```
   INCR tickets_seq
   ```

   → `ticketId`
2. Crear `ticket:{ticketId}` hash:

   ```
   HMSET ticket:{ticketId} id {ticketId} user {user} created_at {ts} event {ev} seat {seat} price {p}
   ```
3. Añadir al índice por usuario:

   ```
   ZADD user:{user}:tickets {ts} {ticketId}
   ```
4. (Opcional) Log de auditoría: `XADD` a stream `tickets:stream` si quieres eventos.

Se recomienda ejecutar pasos 2+3 en una transacción MULTI/EXEC para atomicidad:

```
MULTI
  HMSET ticket:{id} ...
  ZADD user:{user}:tickets {ts} {id}
EXEC
```

Respuesta: devolver ticketId y datos.

---

### 3) `POST /user/logout`

Objetivo: cerrar sesión y permitir nuevo login.

Flujo:

1. Comprobar si usuario está en `connected_users` (opcional).
2. SREM y DEL hash de sesión (en MULTI para consistencia):

```
MULTI
  SREM connected_users {user}
  DEL session:{user}
EXEC
```

Devolver 200 OK.

Nota: si usas `sid` para autenticar requests, verifica que `sid` coincide con `session:{user}.sid` antes de SREM.

---

### 4) `POST /ticket/search` (Listar tickets por usuario)

Objetivo: devolver tickets del usuario, paginados y ordenados.

Comandos:

* Obtener ids (más recientes primero):

  ```
  ZREVRANGE user:{user}:tickets 0 99    // primeros 100
  ```
* Para cada ticketId, obtener datos:

  ```
  HMGET ticket:{ticketId} field1 field2 ...
  ```

Mejor usar `pipeline` para obtener varios HMGET en un solo round-trip.

Ejemplo de paginación:

```
ZREVRANGE user:{user}:tickets <start> <end>
```

---

# Reglas para evitar doble-login (explicadas)

* **SADD atomic**: `SADD connected_users user` te devuelve 1 si el usuario fue añadido (no había), 0 si ya existía. Es una manera rápida y atómica de evitar doble-login.
* **Comprobación del sid**: si permites múltiples dispositivos con diferentes sids, entonces debes modelar sessions como hashes `session:{sid}` y mapear `user -> sid` con `SETNX user:{user}:sid {sid}`. En tu caso quieres impedir 2 logins simultáneos, así que el SET/SADD único por usuario es lo más simple.
* **Protección extra**: si la app puede fallar y no ejecutar logout (e.g. crash), añade TTL a la sesión (`EXPIRE`) y/o un proceso que refresque (keepalive) la sesión.

# Ejemplos concretos (comandos Redis)

**Login (ejemplo):**

```text
> SADD connected_users usuario1
(integer) 1       # ok -> crear sesión
> HSET session:usuario1 sid "uuid-123" login_at "169xxx" ip "1.2.3.4"
(integer) 3
```

Si SADD devuelve 0:

```text
> SADD connected_users usuario1
(integer) 0
# -> devolver 409 "already logged in"
```

**Comprar ticket:**

```text
> INCR tickets_seq
(integer) 101
> MULTI
> HMSET ticket:101 id 101 user usuario1 created_at 169... event "ConciertoX" seat "A1"
> ZADD user:usuario1:tickets 169... 101
> EXEC
```

**Listar tickets (últimos 10):**

```text
> ZREVRANGE user:usuario1:tickets 0 9
1) "101" "58" "23"
# pipeline HMGET ticket:101 ..., ticket:58 ...
```

**Logout:**

```text
> MULTI
> SREM connected_users usuario1
> DEL session:usuario1
> EXEC
```

# Buenas prácticas y opciones avanzadas

* **TTL** en `session:{user}` o refrescar `session` con `EXPIRE` si quieres desconexión automática.
* **Uso de TOKEN/SID**: en vez de usar `user` como key directa para sesión, podrías mapear `user:{user}:sid = sid` con `SETNX` para el mismo efecto; y además tener `session:{sid}` para datos. Con `SETNX` evitas colisiones si prefieres esa semántica.
* **Auditoría**: usa **Redis Streams** (`XADD tickets:stream ...`) para mantener un historial de compras que luego puedas procesar. Esto sería una tercera estructura opcional (pero no requerida).
* **Atomicidad**: para opciones críticas (evitar races complejos) usa **LUA scripts** o `WATCH/MULTI/EXEC`.

# Resumen final (mínimo necesario para tu caso)

* **Estructura 1:** `SET connected_users` → evita doble login.
* **Estructura 2:** `HASH session:{user}` / `HASH ticket:{ticketId}` → guarda detalles de sesión y ticket.
* **Índice:** `ZSET user:{user}:tickets` → lista tickets por usuario ordenados por fecha.

Con esto cumples: endpoints necesarios, verificación de login único, almacenamiento en Redis, almacenar usuario en login, y **usar dos estructuras distintas más un índice**.

Si quieres te escribo los flows de Node-RED (nodos HTTP → nodos Redis) con los comandos exactos y payloads, o te doy el script LUA para hacer el login/logout totalmente atómico — dime si lo quieres y lo hago ya.
