# FastAPI Weather Microservice — Walkthrough

## Summary

Built a complete, production-ready FastAPI microservice that fetches real-time weather data from Open-Meteo, applies unit conversions, and returns validated JSON responses — all files delivered with zero modifications needed.

## Project Structure

```
project-root/
├── .env                              ← OPEN_METEO_BASE_URL
├── requirements.txt                  ← all deps pinned
├── main.py                           ← FastAPI app entry point
├── src/
│   ├── api/weather_router.py         ← GET /weather endpoint
│   ├── services/weather_service.py   ← async httpx + orchestration
│   ├── core/
│   │   ├── config.py                 ← pydantic-settings config
│   │   └── conversions.py            ← pure conversion functions
│   └── schemas/weather.py            ← Pydantic v2 models
└── tests/
    ├── unit/test_conversions.py      ← 8 temp + 7 wind tests
    └── integration/test_weather_endpoint.py ← 13 endpoint tests
```

## Files Delivered

| File | Purpose |
|------|---------|
| [.env](file:///e:/Estudios/CE_IAyBD/SBD/UD10_VibeCoding/.env) | `OPEN_METEO_BASE_URL` |
| [requirements.txt](file:///e:/Estudios/CE_IAyBD/SBD/UD10_VibeCoding/requirements.txt) | All deps with minimum versions |
| [main.py](file:///e:/Estudios/CE_IAyBD/SBD/UD10_VibeCoding/main.py) | FastAPI app + router registration |
| [conversions.py](file:///e:/Estudios/CE_IAyBD/SBD/UD10_VibeCoding/src/core/conversions.py) | `celsius_to_fahrenheit`, `kmh_to_ms` — pure functions |
| [config.py](file:///e:/Estudios/CE_IAyBD/SBD/UD10_VibeCoding/src/core/config.py) | Settings via `pydantic-settings` |
| [weather.py](file:///e:/Estudios/CE_IAyBD/SBD/UD10_VibeCoding/src/schemas/weather.py) | `WeatherResponse`, `ErrorResponse` models |
| [weather_service.py](file:///e:/Estudios/CE_IAyBD/SBD/UD10_VibeCoding/src/services/weather_service.py) | Async httpx client + field validation |
| [weather_router.py](file:///e:/Estudios/CE_IAyBD/SBD/UD10_VibeCoding/src/api/weather_router.py) | `GET /weather` — 200/502 responses |
| [test_conversions.py](file:///e:/Estudios/CE_IAyBD/SBD/UD10_VibeCoding/tests/unit/test_conversions.py) | 15 unit tests (100% core coverage) |
| [test_weather_endpoint.py](file:///e:/Estudios/CE_IAyBD/SBD/UD10_VibeCoding/tests/integration/test_weather_endpoint.py) | 13 integration tests (all mocked) |

## Key Design Decisions

- **Conversion formulas isolated** in `src/core/conversions.py` — never appear in handlers or services
- **Field validation before processing** — checks both `temperature` and `windspeed` exist in Open-Meteo response → 502 if missing
- **Error envelope** — all errors return `{"error": "...", "message": "..."}` with 502 status
- **No raw Open-Meteo JSON** ever reaches the client
- **Modern Pydantic v2** — uses `model_config = SettingsConfigDict(...)` (no deprecated inner `Config` class)

## Test Results

```
28 passed in 5.80s — zero warnings
```

- **15 unit tests**: normal values, 0°C, 0 km/h, negative temps, absolute zero, fractional values, extreme values
- **13 integration tests**: 200 success path (shape, values, no data leakage) + 502 error paths (connection error, timeout, missing fields, server error, envelope shape)

## Running the Service

```bash
# Install deps
py -m pip install -r requirements.txt

# Run tests
py -m pytest tests/ -v

# Start the server
py -m uvicorn main:app --reload
```

Then visit: `http://127.0.0.1:8000/weather`
