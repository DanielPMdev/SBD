# Introducción a MongoDB

> Asignatura: Sistemas de Big Data  
> Curso de Especialización en Inteligencia Artificial y Big Data

## 📌 Descripción
Este bloque temático aborda los fundamentos de las bases de datos NoSQL orientadas a documentos utilizando MongoDB. A través de la experimentación práctica y scripts en Python, se establece un ecosistema contenedorizado para persistir información no relacional y realizar analítica de datos incrustada mediante pipelines de agregación.

## 🎯 Objetivos de Aprendizaje
- Comprender la arquitectura BSON y el modelo basado en documentos (colecciones integradas).
- Implementar contenedores Docker para desplegar nodos de MongoDB localmente.
- Desarrollar scripts de conexión e inserción empleando el framework PyMongo en Python.
- Ejecutar consultas avanzadas, actualizaciones atómicas y operaciones de agregación complejas.

## 🧠 Contenidos
En esta unidad se introduce MongoDB como gestor líder dentro del ámbito Big Data no relacional. Se aborda la creación de colecciones de interés académico (estudiantes, cursos e inscripciones) simulando un entorno universitario. 

### Operaciones CRUD Base
Uso de funciones nativas trasladadas al lenguaje Python (`insert_many`, `find_one`, `update_one`, `delete_one`) para manipular en caliente el estado BSON en el contenedor.

### Pipelines de Agregación Estructurados
Extracción y transformación de datos integrando sub-colecciones. Se trabaja intensamente con las etapas `$lookup` (equiparable a SQL JOIN), `$unwind` para desplegar matrices resultantes, `$group` para agregación volumétrica de datos (media de notas, sumas de inscritos) y `$project` para pulir la vista de los documentos entregados en la salida.

## 🛠️ Tecnologías y Librerías
| Herramienta | Uso en este tema |
|---|---|
| MongoDB | Motor de base de datos no relacional basado en documentos |
| Docker Compose | Tecnología de despliegue para el contenedor de la base de datos |
| Python | Lenguaje de programación conductor |
| `pymongo` | Librería cliente de Python para la capa de abstracción de MongoDB |

## 📁 Archivos
| Archivo | Tipo | Descripción |
|---|---|---|
| `docker-compose.yaml` | Configuración | Fichero IaaC para inicializar la imagen `mongo:latest` con variables de entorno de autenticación. |
| `conexion_mongo.py` | Script Python | Script introductorio que conecta con la base de datos local y realiza un volcado de comprobación básico. |
| `app_mongo_instituto.py` | Script Python | Proyecto core de la unidad. Define la limpieza de datos, inserciones profundas y múltiples consultas y agregaciones interrelacionadas. |
| `DanielPorrasMorales_Actividad_MongoDB_Instituto.pdf` | Apuntes | Enunciado de la actividad práctica orientada al instituto. |
| `DanielPorrasMorales_Actividad_MongoDB_Resuelta.pdf` | Apuntes | Memoria teórica y resolución paso a paso de los procesos documentada. |

## 🚀 Cómo ejecutar (si aplica)
Para desplegar el entorno e interactuar con la base de datos:

```bash
# Levantar el contenedor de MongoDB en background
docker-compose up -d

# Instalar las librerías necesarias
pip install pymongo

# Ejecutar el simulador de datos del instituto
python MongoConexion/app_mongo_instituto.py
```

## 🔗 Relación con otros temas
Este tema sirve como base conceptual para posteriores integraciones en pipelines más complejos en las unidades de flujos de datos (UD5_NodeRed y UD9_Pipelines).
