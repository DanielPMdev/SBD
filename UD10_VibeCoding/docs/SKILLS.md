---
name: fastapi-weather-microservice
description: >
  Build a production-ready FastAPI microservice that queries the Open-Meteo API and returns
  weather data with unit conversions (Celsius→Fahrenheit, km/h→m/s). Use this skill whenever
  the user asks to create, scaffold, or extend a Python/FastAPI microservice that consumes
  external REST APIs, applies business logic transformations, and requires layered architecture,
  Pydantic v2 validation, async HTTP with httpx, and pytest test suites. Also trigger when the
  user asks about unit conversion utilities, error handling patterns for external APIs, or
  structured FastAPI project layouts.
---

# FastAPI Weather Microservice Skill

Builds a **layered, production-ready** FastAPI microservice that:
1. Fetches current weather data from Open-Meteo.
2. Converts temperature (°C → °F) and wind speed (km/h → m/s).
3. Returns a clean, validated JSON response.
4. Handles errors gracefully with a standard error envelope.
5. Is fully tested with `pytest`, using mocks (no real HTTP calls in tests).

---

## 1. Persona & Goal

Act as a **Senior Backend Engineer** expert in Python 3.13+ and scalable API design.

- Write **production-ready code** with robust error handling and precise conversions.
- Guarantee reliability through unit tests.

---

## 2. Tech Stack

| Layer | Tool | Notes |
|---|---|---|
| Language | Python 3.13+ | Mandatory |
| Framework | FastAPI | Latest stable |
| HTTP client | `httpx` (async) | `requests` is **forbidden** |
| Dependency management | `requirements.txt` | — |
| Testing | `pytest` + `pytest-asyncio` + `pytest-mock` | — |
| Data validation | Pydantic v2 | — |
| Config / env vars | `pydantic-settings` + `.env` | — |

---

## 3. Code Standards

- **Type hints** (`typing`) are **mandatory** on all function parameters and return types.
- **Docstrings** in Google format; comment conversion formula logic explicitly.
- **Formatter/Linter:** Follow `Ruff` or `Black` rules. Use single quotes for strings unless double quotes are required.
- **Naming conventions:**
  - `snake_case` → variables, files, functions (e.g., `celsius_to_fahrenheit`)
  - `PascalCase` → classes and Pydantic models (e.g., `WeatherResponse`)
  - `UPPER_SNAKE_CASE` → constants and env var names
- **Language:** Write all code in English.
- **Style:** Clean code, PEP 8 compliant, Single Responsibility Principle (SOLID).
- **Logging:** Use `logging.info` / `logging.error`. **Never use `print()`.**

---

## 4. Project Structure

```
project-root/
├── .env
├── requirements.txt
├── src/
│   ├── api/          # Routers / controllers (FastAPI endpoints)
│   ├── services/     # Business logic + httpx calls to Open-Meteo
│   ├── core/         # Pure math utilities (unit conversion formulas)
│   └── schemas/      # Pydantic v2 models (request/response DTOs)
└── tests/
    ├── unit/         # Pure unit tests for core/ utilities (100% coverage required)
    └── integration/  # Endpoint & service tests (mocked external calls)
```

**Layer rules:**
- `api/` → only routing and HTTP concerns. No business logic.
- `services/` → orchestration and external API calls.
- `core/` → pure functions with zero side effects (easy to unit-test).
- `schemas/` → Pydantic models only; no logic.

---

## 5. Error Handling Protocol

### Standard error envelope (all errors)
```json
{ "error": "error_code", "message": "Human-readable description" }
```

### Required HTTP status codes
| Code | When |
|---|---|
| `200 OK` | Successful query |
| `502 Bad Gateway` | Open-Meteo connection failure, unexpected response, or missing required fields |

### Field validation
Before processing, verify that the Open-Meteo response contains both `temperature` and `windspeed`.  
If either field is missing → return `502` with the standard error envelope.

---

## 6. Business Logic & Integration

### Data source (fixed, do not change)
```
https://api.open-meteo.com/v1/forecast?latitude=39.47&longitude=-0.38&current_weather=true
```

### Mandatory conversions

**Temperature — Celsius → Fahrenheit**
```
T(°F) = T(°C) × (9/5) + 32
```

**Wind speed — km/h → m/s**
```
1 km/h ≈ 0.27778 m/s
```

### Output format
Return **both** values in **both** units:
```json
{
  "temperature": {
    "celsius": 22.5,
    "fahrenheit": 72.5
  },
  "wind_speed": {
    "kmh": 15.0,
    "ms": 4.167
  }
}
```
Never return the raw Open-Meteo JSON. Return only formatted, validated output.

---

## 7. Testing Requirements

### Unit tests (`tests/unit/`)
- **100% coverage** on all `core/` conversion functions.
- Test normal values, edge cases (0°C, 0 km/h), and negative temperatures.

### Integration / endpoint tests (`tests/integration/`)
- Test the FastAPI endpoint response shape and status codes.
- Mock the Open-Meteo HTTP call using `pytest-mock` or `unittest.mock`.
- **No real internet calls** during any test.

### Mock example pattern
```python
# Patch httpx.AsyncClient.get to return a controlled payload
mocker.patch("src.services.weather_service.httpx.AsyncClient.get", return_value=mock_response)
```

---

## 8. Configuration & Security

- Store the Open-Meteo base URL and any future secrets in a `.env` file.
- Load settings via `pydantic-settings`:
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPEN_METEO_BASE_URL: str = "https://api.open-meteo.com/v1/forecast"

    class Config:
        env_file = ".env"
```

---

## 9. Hard Prohibitions ❌

| Prohibited | Reason |
|---|---|
| `import requests` | Synchronous; blocks FastAPI's async event loop |
| Conversion formulas inside route handlers | Violates SRP; untestable in isolation |
| Returning raw Open-Meteo JSON | Breaks the contract; leaks internal details |
| `print()` for logging | Use `logging` module instead |
| Real HTTP calls in tests | Tests must be deterministic and offline |

---

## 10. Quick Implementation Checklist

Follow this order when building or extending the microservice:

- [ ] Scaffold directory structure (`src/api`, `src/services`, `src/core`, `src/schemas`, `tests/`)
- [ ] Create `.env` and `pydantic-settings` config
- [ ] Implement conversion functions in `src/core/` with full docstrings
- [ ] Define Pydantic v2 schemas in `src/schemas/`
- [ ] Build the async `httpx` service in `src/services/`
- [ ] Wire up the FastAPI router in `src/api/`
- [ ] Register the router in `main.py` / `app.py`
- [ ] Write 100% unit tests for `src/core/`
- [ ] Write integration tests with mocked HTTP for `src/services/` and `src/api/`
- [ ] Verify `requirements.txt` lists all dependencies with pinned or minimum versions