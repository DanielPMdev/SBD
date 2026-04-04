"""FastAPI application entry point.

Initializes the FastAPI app and registers all routers.
"""

import logging

from fastapi import FastAPI

from src.api.weather_router import router as weather_router

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

app = FastAPI(
    title='Weather API',
    description='REST API that fetches real-time weather data from Open-Meteo with unit conversions.',
    version='1.0.0',
)

app.include_router(weather_router)
