# Procesamiento y Flujos con Node-RED

> Asignatura: Sistemas de Big Data  
> Curso de Especialización en Inteligencia Artificial y Big Data

## 📌 Descripción
Este bloque se centra en el diseño visual y la orquestación de flujos de datos en arquitecturas integradas utilizando Node-RED. La práctica abarca la extracción de información, su transporte y la manipulación profunda interconectando diversos orígenes y sumideros SQL y NoSQL (PostgreSQL, MongoDB y Redis).

## 🎯 Objetivos de Aprendizaje
- Implementar integraciones de extracción, transformación y carga (ETL) puramente visuales.
- Desplegar una arquitectura multiservicio compleja utilizando `docker-compose`.
- Sintetizar información aleatoria de alto rendimiento con repositorios relacionales para simular sistemas de producción.

## 🧠 Contenidos
El módulo proporciona las plantillas de automatización JSON (flows) esenciales para arrancar una topología de flujo dentro de Node-RED.

A fin de generar un contexto de pruebas verosímil, se incorpora un motor robusto en PostgreSQL capaz de realizar una inyección masiva de cientos de miles de registros aleatorizados simulando operaciones de negocio avanzadas (órdenes, envíos, y pasarelas de pago cruzadas con carteras de clientes). Esto es utilizado directamente por Node-RED como punto de partida en las actividades prácticas, tales como el procesamiento de matrículas o monitorización de sensores de radares.

## 🛠️ Tecnologías y Librerías
| Herramienta | Uso en este tema |
|---|---|
| Node-RED | Plataforma visual de flujos de automatización para IoT y orquestación |
| PostgreSQL | Base de datos relacional para simular ERPs y transacciones |
| MongoDB | Motor documental acoplado a flujos Node-RED |
| Redis Stack | Sistema auxiliar de capa de caché presente en la topología |
| Docker Compose | Gestión de orquestación local del ecosistema integral |

## 📁 Archivos
| Archivo | Tipo | Descripción |
|---|---|---|
| `docker-compose.yaml` | Configuración | Define la topología que orquesta Node-RED, Postgres, Mongo y Redis en una red virtual compartida. |
| `readme.md` | Apuntes | Listado de nodos de Node-RED necesarios (`node-red-contrib-postgresql`, `mongodb4`, exploradores de rutas y un generador aleatorio). |
| `postgres_init/init.sql` | Script SQL | Esquema estructural en PostgreSQL y rutinas `INSERT` masivas procedurales (`generate_series`) para probar rendimiento. |
| `flows_radares_DanielPorrasMorales.json` | Configuración / Datos | Flujo serializado demostrativo para el cruce e ingestión de radares de tráfico. |
| `DanielPorrasMorales_flows.json` | Configuración / Datos | Flujo matriz base del entorno de configuración resuelto. |
| `DanielPorrasMorales_Ejercico_PostgreSQL.docx` | Apuntes | Memoria y especificaciones del conector y consultas SQL. |

## 🚀 Cómo ejecutar (si aplica)
Para desplegar la infraestructura completa base y cargar los flujos por su cuenta:

```bash
# Levantar el stack tecnológico
docker-compose up -d

# Nodos adicionales a instalar en Manage Palette:
# node-red-node-random, node-red-contrib-mongodb4, node-red-contrib-postgresql, node-red-contrib-wait-paths, node-red-node-data-generator

# Acceder vía navegador visual a:
# http://localhost:1880/
```

## 🔗 Relación con otros temas
Hace de puente hacia sistemas en memoria con Redis (UD6) y profundiza en conceptos orquestados introducidos originalmente con MongoDB (UD1).