# Bases de Datos en Memoria con Redis

> Asignatura: Sistemas de Big Data  
> Curso de Especialización en Inteligencia Artificial y Big Data

## 📌 Descripción
Este bloque explora el paradigma evolutivo de las bases de datos NoSQL tipo Clave-Valor en memoria mediante **Redis**. Se centra en el diseño de arquitecturas de altísimo rendimiento orientadas a latencias de submilisegundo, necesarias para rastreo en tiempo real, memorias de caché distribuidas y control estricto de concurrencia en sesiones.

## 🎯 Objetivos de Aprendizaje
- Comprender y diferenciar las estructuras de datos nativas en Redis (SET, HASH, ZSET).
- Implementar proyectos Python independientes conectados a Redis para almacenamiento temporal y de estados.
- Integrar múltiples bases de datos concurrentes (Redis + MongoDB + PostgreSQL) según la naturaleza de la consulta.
- Garantizar atomicidad transaccional evadiendo condiciones de carrera (ej. logins simultáneos).

## 🧠 Contenidos
Esta unidad se fundamenta en la resolución de dos grandes problemas o casos de uso prácticos, divididos en tres directorios:

1. **Rastreo y Monitorización Vehicular** (`CarSensor` y `CarTracker`):
Sistemas que procesan todos los eventos telemétricos de vehículos, almacenándolos de manera óptima para tres modos de explotación: 
   - Histórico inmutable (derivado a MongoDB).
   - Contabilización y métricas acumulativas de paso (PosgreSQL).
   - Estado ultra-rápido del *último* sensor transitado por un vehículo concreto (Redis).

2. **Backend de Ticketing Segurizado** (`Tickets`):
Simulación interactiva de una API transaccional de ventas utilizando estructuras Redis como fuente principal de verdad. Demuestra el control de autenticación mediante SETs (`connected_users` para evadir doble login simultáneo), HASHes para perfilar la sesión y JSON con ÍNDICES (`ZSET`) por timestamp para enumerar y buscar perfiles de compras sin impactar el disco.

## 🛠️ Tecnologías y Librerías
| Herramienta | Uso en este tema |
|---|---|
| Redis Stack | Motor en memoria Clave-Valor y JSON |
| Python | Código fuente de los demonios procesadores |
| `redis` (py) | Controlador de conexiones asíncronas de base de datos |
| Docker Compose | Aprovisionamiento estandarizado del bus de servicios |

## 📁 Archivos y Subdirectorios Principales
| Archivo / Carpeta | Tipo | Descripción |
|---|---|---|
| `CarSensor/` | Proyecto Python | Rastreador base ingiriendo mediante websockets y grabando el último estado de paso. |
| `CarTracker/` | Proyecto Python | Motor paralelo que implementa un productor y consumidor acoplado a Redis. |
| `Tickets/` | Entorno | API Node-RED y NGINX con apuntes exhaustivos de las transacciones atómicas LUA de Redis. |
| `Tickets/apuntes.md` | Apuntes | Explicación profunda de los esquemas estructurales atómicos usados. |

## 🚀 Cómo ejecutar (Ejemplo: CarSensor / CarTracker)
Dado que los módulos de rádares son proyectos Python independientes estructurados, su ejecución típica se lanza desde la respectiva subcarpeta:

```bash
# Entorno virtual y dependencias (ejecutar en la carpeta contenedora)
cd CarSensor  # o CarTracker
pip install -r requirements.txt

# Copiar configuración inicial de las bases de datos
cp .env.example .env

# Levantar infraestructura (Redis, Mongo, Postgres)
cd docker
docker-compose up -d

# Arrancar el programa principal
cd ..
python src/main.py
```

## 🔗 Relación con otros temas
Integra PostgreSQL y MongoDB estudiados en instancias previas (UD1 y UD5) operando de forma paralela en roles muy heterogéneos y fuertemente desacomplados.
