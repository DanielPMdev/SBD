# Bases de Datos Orientadas a Grafos con Neo4j

> Asignatura: Sistemas de Big Data  
> Curso de Especialización en Inteligencia Artificial y Big Data

## 📌 Descripción
Esta unidad temática aborda el ecosistema de las bases de datos NoSQL basadas en teoría de Grafos, concretamente utilizando Neo4j. El enfoque primordial es modelar datos cuyo verdadero valor reside en la relación intrínseca y la conectividad (redes sociales, recomendaciones, adyacencias) más que en su propia estructura de atributos.

## 🎯 Objetivos de Aprendizaje
- Comprender mentalmente la morfología de nodos, aristas (relaciones) y etiquetas.
- Dominar la sintaxis y ejecución del lenguaje de consulta moderno `Cypher`.
- Desarrollar e interrogar redes sociales complejas encontrando patrones implícitos y grados de separación temporal.

## 🧠 Contenidos
La resolución discurre modelando el núcleo de un sistema social básico poblado por Usuarios (nodos `User`) que generan Publicaciones (nodos `Post`).
Se establece un entramado denso y dirigido de interacciones utilizando vínculos semánticos tales como `[:FRIEND_OF]`, `[:FOLLOWS]`, `[:POSTED]` y `[:LIKED]`.

A partir de este escenario orgánico, se practican consultas Cypher para:
- Detectar clústeres de afinidad.
- Filtrar proyecciones adyacentes de grafo cruzado (¿A quién siguen los seguidores de un usuario?).
- Extraer grados de interconexión (amigos de amigos).
- Búsquedas con saltos de profundidad variable (`[*1..3]`).

## 🛠️ Tecnologías y Librerías
| Herramienta | Uso en este tema |
|---|---|
| Neo4j | DBMS nativo orientado a propiedades de grafos transaccionales |
| Cypher | Lenguaje declarativo de patrones para interrogar la red |
| Docker Compose | Provisión del servicio gráfico `neo4j` y su interfaz web (Browser) |

## 📁 Archivos Principales
| Archivo / Carpeta | Tipo | Descripción |
|---|---|---|
| `docker-compose.yml` | Configuración | Plantilla de levantamiento autónomo de Neo4j en un contenedor para evitar instalaciones ensuciando la máquina. |
| `RedSocial/Consultas_DanielPorrasMorales.txt` | Script Cypher | Sentencias DML base `CREATE` masivas y patrones `MATCH-RETURN` resueltos por el alumno evidenciando asimilación. |
| `RedSocial/documentacion.odt` | Apuntes | Entregable de formato textual con la memoria del proyecto social. |
| `Consultas/Consultas Neo4j...docx` | Apuntes | Respuestas directas a consultas Cypher formuladas sobre diagramas de grafo aislados. |

## 🚀 Cómo ejecutar
Dado que no existe acoplamiento vía driver en lenguajes intermedios y las consultas se lanzan manualmente, la ejecución consiste en aprovisionar la interfaz:

```bash
# Arrancar el clúster local de grafos
docker-compose up -d

# Acceder al Neo4j Browser interactivo en:
# http://localhost:7474/
# Usuario/Passwd configurados en el fichero de entorno.
```

## 🔗 Relación con otros temas
Muestra una perspectiva diametralmente opuesta al ruteo documental y estructurado abordado de SQL u otras formas de NoSQL (Mongo, Redis) previamente en el curso.
