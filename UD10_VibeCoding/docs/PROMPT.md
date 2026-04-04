You are a Senior Backend Engineer expert in Python 3.13+ and scalable API design.

Build a complete, production-ready FastAPI microservice following the architecture and 
standards defined below. Deliver all files ready to run with zero modifications.

---

## OBJECTIVE

Create a REST API that fetches real-time weather data from Open-Meteo, applies unit 
conversions, and returns a clean, validated JSON response.

---

## TECHNICAL STANDARDS (non-negotiable)

**Stack:**
- Python 3.13+, FastAPI, httpx (async) — requests is FORBIDDEN
- Pydantic v2 for validation, pydantic-settings for config
- pytest + pytest-asyncio + pytest-mock for testing

**Code style:**
- Mandatory type hints on all functions and return types
- Google-format docstrings; comment conversion formulas explicitly
- Follow Ruff/Black rules, single quotes, English only
- snake_case for functions/files/variables, PascalCase for classes/models, 
  UPPER_SNAKE_CASE for constants
- logging.info / logging.error only — print() is FORBIDDEN

---

## PROJECT STRUCTURE

Generate exactly this layout:

project-root/
├── .env
├── requirements.txt
├── main.py
├── src/
│   ├── api/          # FastAPI routers only — no business logic here
│   ├── services/     # Orchestration + httpx calls to Open-Meteo
│   ├── core/         # Pure conversion functions (zero side effects)
│   └── schemas/      # Pydantic v2 models only
└── tests/
    ├── unit/         # 100% coverage on src/core/
    └── integration/  # Endpoint + service tests, all HTTP calls mocked

---

## DATA SOURCE (fixed — do not change)

GET https://api.open-meteo.com/v1/forecast?latitude=39.47&longitude=-0.38&current_weather=true

Store the base URL in .env and load it via pydantic-settings.

---

## MANDATORY CONVERSIONS

Use EXCLUSIVELY these formulas, implemented as pure functions in src/core/:

  Temperature:  F = (C × 9/5) + 32
  Wind speed:   V_ms = V_kmh ÷ 3.6

Formulas must NEVER appear inside route handlers or service methods.
They must be independently testable in isolation.

---

## API CONTRACT

Single endpoint: GET /weather

Success response (200 OK):
{
  "temperature": {
    "celsius": <float>,
    "fahrenheit": <float>
  },
  "wind_speed": {
    "kmh": <float>,
    "ms": <float>
  }
}

Error response envelope (used for ALL errors):
{ "error": "error_code", "message": "Human-readable description" }

Error codes:
- 502 Bad Gateway → Open-Meteo unreachable, unexpected response, 
  or missing "temperature" / "windspeed" fields in payload.

Validate that both "temperature" and "windspeed" exist in the 
Open-Meteo response before processing. If either is absent → 502.
Never return raw Open-Meteo JSON.

---

## TESTING REQUIREMENTS

Unit tests (tests/unit/):
- 100% coverage on all src/core/ conversion functions
- Cover: normal values, zero inputs (0°C, 0 km/h), negative temperatures

Integration tests (tests/integration/):
- Test GET /weather response shape and status codes (200, 502)
- Mock httpx.AsyncClient using pytest-mock — NO real HTTP calls in any test
- Test the 502 path when Open-Meteo returns a payload missing required fields

---

## DELIVERABLES CHECKLIST

Produce every file below, fully implemented (no TODOs, no placeholders):

[ ] .env                          ← OPEN_METEO_BASE_URL defined
[ ] requirements.txt              ← all deps with minimum versions pinned
[ ] main.py                       ← FastAPI app entry point
[ ] src/core/conversions.py       ← pure conversion functions + docstrings
[ ] src/schemas/weather.py        ← Pydantic v2 response model
[ ] src/services/weather_service.py  ← async httpx client + orchestration
[ ] src/api/weather_router.py     ← FastAPI router, wires service to endpoint
[ ] tests/unit/test_conversions.py   ← 100% unit coverage on core/
[ ] tests/integration/test_weather_endpoint.py  ← mocked integration tests

Output each file with its full path as a header, followed by the complete file content.

SKILLS.md

PRD_Weather_AI_API_Specs.md