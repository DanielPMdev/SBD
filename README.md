# Sistemas de Big Data

> 📚 Curso de Especialización en Inteligencia Artificial y Big Data  
> 🏫 IES Abastos

## 📖 Sobre esta asignatura
Este repositorio compila todos los materiales formativos, ejercicios prácticos y proyectos arquitectónicos de la asignatura **Sistemas de Big Data**. El itinerario persigue dotar al estudiante de un perfil robusto en ingeniería de datos, modelado NoSQL, orquestación de flujos integrados, visualización empresarial y analítica predictiva en tiempo real orientada a streaming (ETL moderno).

## 🗂️ Estructura del repositorio

```
📦 Sistemas de Big Data
 ┣ 📂 UD1_MongoDB
 ┃ ┣ 📓 DanielPorrasMorales_Actividad_MongoDB_Instituto.pdf
 ┃ ┣ 🐍 MongoConexion/app_mongo_instituto.py
 ┃ ┣ ⚙️ docker-compose.yaml
 ┃ ┗ 📋 README.md
 ┣ 📂 UD2_GIT
 ┃ ┣ 📄 DanielPorrasMorales_Actividad_GitTraining.pdf
 ┃ ┗ 📋 README.md
 ┣ 📂 UD5_NodeRed
 ┃ ┣ ⚙️ docker-compose.yaml
 ┃ ┣ 📄 postgres_init/init.sql
 ┃ ┣ 📓 flows_radares_DanielPorrasMorales.json
 ┃ ┗ 📋 README.md
 ┣ 📂 UD6_Redis
 ┃ ┣ 📂 CarSensor
 ┃ ┣ 📂 CarTracker
 ┃ ┣ 📂 Tickets
 ┃ ┗ 📋 README.md
 ┣ 📂 UD7_Neo4j
 ┃ ┣ ⚙️ docker-compose.yml
 ┃ ┣ 📄 RedSocial/Consultas_DanielPorrasMorales.txt
 ┃ ┗ 📋 README.md
 ┣ 📂 UD8_PowerBI
 ┃ ┣ 📊 most_valuable_teams.csv
 ┃ ┣ 📈 EquiposMasValiosos.pbix
 ┃ ┣ 📈 IES_Abastos.pbix
 ┃ ┗ 📋 README.md
 ┣ 📂 UD9_Pipelines
 ┃ ┣ 📂 factory-etl
 ┃ ┃ ┣ 🐍 src/simulator.py
 ┃ ┃ ┣ 🐍 src/processor.py
 ┃ ┃ ┗ ⚙️ docker-compose.yaml
 ┃ ┗ 📋 README.md
 ┗ 📋 README.md
```

## 📚 Bloques Temáticos

### 1. Introducción a MongoDB
📂 [`UD1_MongoDB/`](./UD1_MongoDB/)

Introducción y fundamentos en bases de datos orientadas a documentos (BSON), realizando consultas CRUD integrativas y tuberías de agregación abstractas.

**Conceptos clave:** `Colecciones` · `Pipelines de Agregación` · `$lookup`  
**Tecnologías:** `MongoDB` · `PyMongo` · `Docker`

---

### 2. Entrenamiento en Git
📂 [`UD2_GIT/`](./UD2_GIT/)

Bloque instrumental focalizado en dominar la estructura histórica, instantáneas, subida a repositorios remotos y la lógica distribuida.

**Conceptos clave:** `Commit` · `Branching` · `Control de Versiones`  
**Tecnologías:** `Git`

---

### 5. Procesamiento y Flujos con Node-RED
📂 [`UD5_NodeRed/`](./UD5_NodeRed/)

Generación visual de modelos ETL. Conecta entornos y propaga grandes volúmenes de datos simulados a través de bases PostgreSQL y almacenes de datos alternativos.

**Conceptos clave:** `ETL` · `Flujos` · `Inyección Masiva SQL`  
**Tecnologías:** `Node-RED` · `PostgreSQL` · `JSON`

---

### 6. Bases de Datos en Memoria con Redis
📂 [`UD6_Redis/`](./UD6_Redis/)

Modelos ultra rápidos (tiempo real) implementando la lógica en memoria principal para radares y evadiendo cuellos de botella mediante proyectos Python independientes (e.g. backend de venta de tickets sin falsos paralelos).

**Conceptos clave:** `KV-Store` · `Pub/Sub` · `Atomicidad SETs`  
**Tecnologías:** `Redis Stack` · `Python` · `Websockets`

---

### 7. Orientación a Grafos con Neo4j
📂 [`UD7_Neo4j/`](./UD7_Neo4j/)

El núcleo del ecosistema son sus relaciones. Modelización intensiva de un entorno de redes sociales simulado, extrayendo patrones semánticos directos de sus conexiones adyacentes.

**Conceptos clave:** `Grafos` · `Nodos` · `Adyacencia`  
**Tecnologías:** `Neo4j` · `Cypher`

---

### 8. Análisis y Modelado Visual con Power BI
📂 [`UD8_PowerBI/`](./UD8_PowerBI/)

Unidad dedicada exhaustivamente al Business Intelligence, ingesta tabular de reportes Excel/CSV (Titanic, institutos, finanzas) y transposición visual mediante cuadros de mando accionables (Dashboards).

**Conceptos clave:** `Dashboards` · `DAX` · `Modelado Semántico`  
**Tecnologías:** `Microsoft Power BI` · `CSV/Excel`

---

### 9. Tuberías de Datos ETL (Streaming)
📂 [`UD9_Pipelines/`](./UD9_Pipelines/)

Cúspide de la asignatura, donde se desarrolla de cero y de manera robusta una tubería conectando a fábricas perimetrales simuladas emitiendo en Kafka y volcando en Kibana. Todo bajo controladores orquestados por Python customizado.

**Conceptos clave:** `ETL en Vuelo` · `Broker Mensajería` · `Indexado Masivo`  
**Tecnologías:** `Apache Kafka` · `ElasticSearch` · `Kibana`

## 🧰 Stack Tecnológico General

| Tecnología | Rol |
|---|---|
| Python | Lenguaje vehicular universal en analítica subyacente y simulación |
| Docker & Docker-Compose | Aprovisionadores unificados de todo el clúster (IaaC) |
| MongoDB | Persistencia en frío NoSQL de archivos |
| PostgreSQL | Motor persistente en capa analítica de transacciones relacionales |
| Redis Stack | Memoria caché intersecante y bases de datos transitorias |
| Neo4j | Visualizador relacional de entidades y grafos atados directamente |
| Kafka | Bus de mensajes ininterrumpido a modo Streaming Buffer (`Broker`) |
| ElasticSearch & Kibana | Indexador y visualizador consumiendo el ETL originado de Python |
| Power BI | Visualización en diferido resolviendo casos estáticos con macros |
| Node-RED | Abstracción visual para integradores ETL (`Low code`) |
| Git | Controlador de todo el versionado originario de los ficheros físicos |

## 🗺️ Orden de estudio recomendado
Para alcanzar una óptima comprensión evolutiva orientada a las arquitecturas puras de datos (sin incluir ofimática separada o modelado frontend), el recorrido lógico se ajusta firmemente a la progresión impuesta:

1. **UD2 y UD1**: Bases metodológicas (Git) y conceptuales (BSON en Mongo).
2. **UD5**: Traslado transversal conectando nodos visuales simulando Big Data en PostgreSQL.
3. **UD6 y UD7**: Desglose especializado de motores ultra veloces (Redis) o altamente entrelazados (Neo4j).
4. **UD9**: El compendio integrador orquestador por excelencia (Kafka + ETL Pipeline).
5. **UD8**: Visualización interpretativa asíncrona final una vez garantizado el origen (Power BI).

## 📝 Notas
- Los materiales de esta asignatura son de carácter estrictamente educativo.
- Para el levantamiento de clústeres simultáneos, se aconseja una dotación mínima de memoria en contenedores Docker de al menos 4 GB (especialmente notable en Elasticsearch y Kafka).
