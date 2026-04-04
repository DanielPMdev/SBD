"""FastAPI router for weather endpoints.

Contains only routing and HTTP concerns — no business logic.
Delegates all work to the weather service layer.
"""

import logging

import httpx
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.schemas.weather import ErrorResponse, WeatherResponse
from src.services.weather_service import get_current_weather

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    '/weather',
    response_model=WeatherResponse,
    responses={
        502: {'model': ErrorResponse, 'description': 'Open-Meteo API error'},
    },
    summary='Get current weather data',
    description='Fetches real-time weather from Open-Meteo and returns temperature and wind speed in multiple units.',
)
async def get_weather() -> WeatherResponse | JSONResponse:
    """Handle GET /weather requests.

    Returns:
        WeatherResponse on success, or a 502 JSONResponse on failure.
    """
    try:
        weather_data = await get_current_weather()
        return weather_data
    except (httpx.RequestError, httpx.HTTPStatusError) as exc:
        logging.error('Open-Meteo API request failed: %s', exc)
        return JSONResponse(
            status_code=502,
            content=ErrorResponse(
                error='bad_gateway',
                message='Could not connect to Open-Meteo service.',
            ).model_dump(),
        )
    except KeyError as exc:
        logging.error('Open-Meteo response validation failed: %s', exc)
        return JSONResponse(
            status_code=502,
            content=ErrorResponse(
                error='bad_gateway',
                message='Open-Meteo returned an unexpected response format.',
            ).model_dump(),
        )
    except Exception as exc:
        logging.error('Unexpected error fetching weather data: %s', exc)
        return JSONResponse(
            status_code=502,
            content=ErrorResponse(
                error='bad_gateway',
                message='An unexpected error occurred while fetching weather data.',
            ).model_dump(),
        )
