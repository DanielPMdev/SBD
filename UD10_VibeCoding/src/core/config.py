"""Application settings loaded from environment variables.

Uses pydantic-settings to read from .env file.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from .env file."""

    model_config = SettingsConfigDict(env_file='.env')

    OPEN_METEO_BASE_URL: str = 'https://api.open-meteo.com/v1/forecast'


settings = Settings()
