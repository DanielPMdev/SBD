"""Weather service — orchestration layer for Open-Meteo API calls.

Handles async HTTP communication with the Open-Meteo API and applies
business logic transformations via core conversion functions.
"""

import logging

import httpx

from src.core.config import settings
from src.core.conversions import celsius_to_fahrenheit, kmh_to_ms
from src.schemas.weather import (
    TemperatureResponse,
    WeatherResponse,
    WindSpeedResponse,
)

logger = logging.getLogger(__name__)

# Fixed query parameters for the Open-Meteo forecast endpoint
OPEN_METEO_QUERY_PARAMS: dict[str, str] = {
    'latitude': '39.47',
    'longitude': '-0.38',
    'current_weather': 'true',
}


async def get_current_weather() -> WeatherResponse:
    """Fetch current weather from Open-Meteo and return converted data.

    Queries the Open-Meteo API for current weather at the configured
    coordinates (Valencia, Spain), validates the response, applies unit
    conversions, and returns a structured WeatherResponse.

    Returns:
        WeatherResponse with temperature (°C + °F) and wind speed (km/h + m/s).

    Raises:
        httpx.HTTPStatusError: If the Open-Meteo API returns a non-2xx status.
        KeyError: If the response payload is missing required fields.
        httpx.RequestError: If the request fails due to network issues.
    """
    async with httpx.AsyncClient() as client:
        logging.info(
            'Fetching weather data from %s', settings.OPEN_METEO_BASE_URL
        )
        response = await client.get(
            settings.OPEN_METEO_BASE_URL,
            params=OPEN_METEO_QUERY_PARAMS,
        )
        response.raise_for_status()

    data = response.json()
    current_weather = data.get('current_weather', {})

    # Validate that both required fields exist in the response
    if 'temperature' not in current_weather or 'windspeed' not in current_weather:
        logging.error(
            'Open-Meteo response missing required fields. Payload: %s', data
        )
        raise KeyError(
            'Open-Meteo response missing "temperature" or "windspeed" fields'
        )

    celsius: float = float(current_weather['temperature'])
    kmh: float = float(current_weather['windspeed'])

    logging.info(
        'Received weather data — temperature: %.2f°C, wind: %.2f km/h',
        celsius,
        kmh,
    )

    return WeatherResponse(
        temperature=TemperatureResponse(
            celsius=celsius,
            fahrenheit=celsius_to_fahrenheit(celsius),
        ),
        wind_speed=WindSpeedResponse(
            kmh=kmh,
            ms=round(kmh_to_ms(kmh), 3),
        ),
    )
