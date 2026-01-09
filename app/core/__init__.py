"""Core utilities and settings for YouLogiX."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	project_name: str = "YouLogiX"


settings = Settings()

__all__ = ["Settings", "settings"]
