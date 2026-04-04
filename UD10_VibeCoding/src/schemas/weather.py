"""Pydantic v2 models for weather API request/response schemas.

Contains all data transfer objects (DTOs) used by the API layer.
No business logic — models only.
"""

from pydantic import BaseModel


class TemperatureResponse(BaseModel):
    """Temperature data in both Celsius and Fahrenheit."""

    celsius: float
    fahrenheit: float


class WindSpeedResponse(BaseModel):
    """Wind speed data in both km/h and m/s."""

    kmh: float
    ms: float


class WeatherResponse(BaseModel):
    """Successful weather response containing temperature and wind speed."""

    temperature: TemperatureResponse
    wind_speed: WindSpeedResponse


class ErrorResponse(BaseModel):
    """Standard error envelope for all API errors."""

    error: str
    message: str
