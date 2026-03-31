# Tuberías de Datos ETL (Streaming)

> Asignatura: Sistemas de Big Data  
> Curso de Especialización en Inteligencia Artificial y Big Data

## 📌 Descripción
Esta unidad es el proyecto integrador o eslabón definitivo que aúna las mecánicas vistas anteriormente bajo un entorno industrial simulado de tiempo real (Streaming). En ella se instaura un Pipeline de extracción, transformación y carga fluida orquestado por clústeres Apache Kafka que remata en repositorios para su lectura masiva y analítica usando ElasticSearch y Kibana de manera ininterrumpida.

## 🎯 Objetivos de Aprendizaje
- Arquitectar de forma pragmática la capa de mensajería asíncrona robusta utilizando un clúster Kafka (Brokers / KRaft).
- Generar simuladores procedimentales (Producers) de eventos distribuidos de volumetría alta.
- Estructurar consumidores ETL programáticos en Python orientados al procesado perimetral e ingesta final nativa en Search Engines.
- Familiarizarse analíticamente con el ecosistema visual de Kibana.

## 🧠 Contenidos
Todo gira en torno a un escenario consolidado en la carpeta principal `factory-etl`:

### Simulación Funcional Distribuida
Un entramado industrial donde decenas de sensores de diferentes nodos o maquinarias (`UNS56A` Posicionador, `FB713A` Llenadora, `CPM784` Taponadora...) reportan cíclicamente atributos operacionales (luz, litros, temperatura) a un tópico maestro.

### Procesador / Consumidor Agregador
Una aplicación robusta conectada en caliente al clúster de ingesta de origen, capaz de desencriptar las trazas semánticas crudas que envían los sensores, traducirlas mediante un glosario programado internamente, transformarlas a JSON legible y acomodarlas (índices diarios) atómicamente contra el motor de ElasticSearch en el servidor web correspondiente.

## 🛠️ Tecnologías y Librerías
| Herramienta | Uso en este tema |
|---|---|
| Apache Kafka | Bus (Broker) de orquestación de mensajes y eventos en tiempo real |
| KRaft | Protocolo intrínseco de cuórum en Kafka sin usar Zookeeper externo |
| Kafdrop | UI visual en navegador para monitorizar el volumen de ingesta del clúster |
| ElasticSearch | Search engine final y servidor de indexación analítica (`localhost:9200`) |
| Kibana | Plataforma visual analítica y administrativa por excelencia conectada a Elastic (`localhost:5601`) |
| Python (`confluent-kafka`) | Cliente de alta robustez para la capa ETL perimetral customizada |

## 📁 Archivos
| Archivo | Tipo | Descripción |
|---|---|---|
| `factory-etl/docker-compose.yaml` | Configuración | Plantilla masiva con despliegue de 5 servicios (Kafka, Kafdrop, ES, Kibana y opcionales Python dockerizados). |
| `factory-etl/src/simulator.py` | Script Python | Simula la planta. Fabrica y emite eventos ilegibles y frenéticos hacia `factory.machines.telemetry`. |
| `factory-etl/src/processor.py` | Script Python | Absorbe el flujo de la cola, serializa al castellano sus claves semánticas e inyecta rítmicamente. |
| `factory-etl/src/pipeline/` y `utils/` | Módulo Python | Paquetería modular de soporte, conexión de bases de datos y test suites. |
| `factory-etl/README.md` | Apuntes | Diccionario semántico descriptivo sobre los diccionarios y glosarios programados. |

## 🚀 Cómo ejecutar
La simulación está paquetizada por defecto para levantarse cómodamente de forma mixta (infraestructura container y procesadores nativos mediante virtual env):

```bash
# 1. Levantar Kafka y su ecosistema (ignorar warnings si los python no levantan)
cd factory-etl
docker-compose up -d

# 2. Recrear el entorno ejecutable nativo
python -m venv .venv
# source .venv/bin/activate
# O en Windows:
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env

# 3. Lanzar la capa física/telemetría (abrir en una terminal y dejar abierta)
python src/simulator.py

# 4. Lanzar la capa transformacional intermedia ETL (abrir en otra terminal y dejar abierta)
python src/processor.py
```
