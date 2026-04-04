# Vibe Coding — Microservicio Meteorológico con FastAPI

> Asignatura: Sistemas de Big Data  
> Curso de Especialización en Inteligencia Artificial y Big Data

## 📌 Descripción
Esta unidad introduce el concepto de **Vibe Coding**: el desarrollo de software completo asistido por modelos de Inteligencia Artificial. El caso práctico consiste en la construcción de un microservicio REST con FastAPI que consume datos meteorológicos en tiempo real de la API pública Open-Meteo, aplica conversiones de unidades (temperatura y velocidad del viento) y expone los resultados a través de un endpoint validado con Pydantic v2. El proyecto sigue una arquitectura por capas (Layered Architecture), incluye manejo robusto de errores y está respaldado por una suite completa de tests unitarios e integración.

## 🎯 Objetivos de Aprendizaje
- Comprender el paradigma de **Vibe Coding** y la generación de código asistida por IA mediante prompts estructurados.
- Implementar un microservicio REST profesional con **FastAPI** y comunicación asíncrona vía **httpx**.
- Aplicar una **arquitectura por capas** (Layered Architecture) separando routing, servicios, lógica pura y schemas.
- Diseñar **funciones puras** para conversiones de unidades, testeables de forma aislada.
- Validar datos de entrada y salida con **Pydantic v2** y gestionar configuración con **pydantic-settings**.
- Implementar un protocolo de **manejo de errores estandarizado** con envelope JSON y códigos HTTP (200/502).
- Escribir **tests unitarios** (100% cobertura en lógica de negocio) y **tests de integración** con mocks (sin llamadas reales a red).

## 🧠 Contenidos

### Vibe Coding y Desarrollo Asistido por IA
El Vibe Coding es una metodología de desarrollo en la que el programador define la arquitectura, los estándares y las restricciones del proyecto mediante **prompts detallados**, y delega la generación del código a un modelo de IA. El resultado es un proyecto funcional que cumple las especificaciones técnicas proporcionadas. En esta unidad se documentan los prompts exactos utilizados, los documentos de requisitos (PRD) y las habilidades (SKILLS) que guiaron la generación del código.

### Arquitectura del Microservicio
El proyecto sigue una **arquitectura por capas** con separación estricta de responsabilidades:

- **Capa API (`src/api/`):** Routers de FastAPI que gestionan exclusivamente la entrada/salida HTTP. No contienen lógica de negocio.
- **Capa de Servicios (`src/services/`):** Orquestación y comunicación asíncrona con la API externa Open-Meteo mediante `httpx.AsyncClient`.
- **Capa Core (`src/core/`):** Funciones puras de conversión de unidades (sin efectos secundarios) y configuración de la aplicación vía `pydantic-settings`.
- **Capa de Schemas (`src/schemas/`):** Modelos Pydantic v2 (DTOs) para la validación y serialización de respuestas.

### Conversiones de Unidades
Se implementan como funciones puras independientes en `src/core/conversions.py`:

- **Temperatura:** `F = (C × 9/5) + 32` — Celsius a Fahrenheit.
- **Velocidad del viento:** `V_ms = V_kmh ÷ 3.6` — Kilómetros por hora a metros por segundo.

### Protocolo de Errores
Toda respuesta de error sigue un envelope JSON estandarizado:
```json
{ "error": "error_code", "message": "Descripción legible del error" }
```
Se valida que la respuesta de Open-Meteo contenga los campos `temperature` y `windspeed` antes de procesar. Si faltan, se devuelve un `502 Bad Gateway`.

### Testing
- **Tests unitarios (`tests/unit/`):** 15 tests con cobertura del 100% sobre las funciones de conversión, cubriendo valores normales, cero, negativos, fraccionales y extremos (cero absoluto).
- **Tests de integración (`tests/integration/`):** 13 tests que verifican el endpoint `GET /weather` con mocks de `httpx.AsyncClient`. Cubren respuestas exitosas (200), errores de conexión, timeout, campos faltantes y errores de servidor (502).

## 🛠️ Tecnologías y Librerías
| Herramienta | Uso en este tema |
|---|---|
| Python 3.13+ | Lenguaje principal del microservicio |
| FastAPI | Framework para la API REST asíncrona |
| httpx | Cliente HTTP asíncrono para consumir Open-Meteo |
| Pydantic v2 | Validación y serialización de datos (DTOs) |
| pydantic-settings | Gestión de configuración desde archivo `.env` |
| pytest | Framework de testing |
| pytest-asyncio | Soporte para tests asíncronos |
| pytest-mock | Mocking de llamadas HTTP en tests |
| uvicorn | Servidor ASGI para ejecutar la aplicación |
| logging | Registro de eventos (prohibido usar `print()`) |

## 📁 Archivos
| Archivo | Tipo | Descripción |
|---|---|---|
| `main.py` | Script Python | Punto de entrada de la aplicación FastAPI; registra los routers |
| `requirements.txt` | Configuración | Dependencias del proyecto con versiones mínimas |
| `.env` | Configuración | Variable de entorno `OPEN_METEO_BASE_URL` |
| `src/api/weather_router.py` | Script Python | Router del endpoint `GET /weather` con manejo de errores 200/502 |
| `src/services/weather_service.py` | Script Python | Servicio asíncrono que consume Open-Meteo, valida respuesta y aplica conversiones |
| `src/core/conversions.py` | Script Python | Funciones puras de conversión: `celsius_to_fahrenheit` y `kmh_to_ms` |
| `src/core/config.py` | Script Python | Configuración de la aplicación con `pydantic-settings` |
| `src/schemas/weather.py` | Script Python | Modelos Pydantic v2: `WeatherResponse`, `TemperatureResponse`, `WindSpeedResponse`, `ErrorResponse` |
| `tests/unit/test_conversions.py` | Test Python | 15 tests unitarios para funciones de conversión (100% cobertura) |
| `tests/integration/test_weather_endpoint.py` | Test Python | 13 tests de integración del endpoint con mocks |
| `docs/PROMPT.md` | Documentación | Prompt principal utilizado para la generación del código con IA |
| `docs/PRD_Weather_AI_API_Specs.md` | Documentación | Documento de requisitos del producto (PRD) |
| `docs/SKILLS.md` | Documentación | Definición de habilidades y estándares del microservicio |
| `docs/info.md` | Documentación | Especificaciones técnicas detalladas del proyecto |
| `docs/walkthrough.md` | Documentación | Resumen del proceso de construcción y resultados de tests |
| `docs/Building FastAPI Weather Microservice.md` | Documentación | Registro de la conversación con IA durante el desarrollo |

## 🚀 Cómo ejecutar

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la suite de tests (28 tests — sin conexión a internet)
python -m pytest tests/ -v

# Iniciar el servidor de desarrollo
python -m uvicorn main:app --reload
```

Una vez iniciado, el endpoint estará disponible en:
- **API:** `http://127.0.0.1:8000/weather`
- **Documentación Swagger:** `http://127.0.0.1:8000/docs`

**Ejemplo de respuesta exitosa (200 OK):**
```json
{
  "temperature": {
    "celsius": 18.5,
    "fahrenheit": 65.3
  },
  "wind_speed": {
    "kmh": 12.0,
    "ms": 3.333
  }
}
```

## 🔗 Relación con otros temas
Esta unidad representa la aplicación transversal de competencias adquiridas a lo largo de la asignatura. A diferencia de las unidades anteriores que se centran en bases de datos y procesamiento de datos, aquí se construye un **servicio consumidor de APIs externas** siguiendo estándares profesionales. El enfoque de Vibe Coding complementa el aprendizaje técnico con una metodología de desarrollo emergente basada en IA, conectando con las habilidades de ingeniería de datos y arquitectura de software trabajadas en unidades como UD9 (Pipelines ETL) y UD6 (Redis — microservicios Python).
