# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     DATABASE_URL: str

#     class Config:
#         env_file = ".env"

# settings = Settings()
# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    DATABASE_URL: str
    APP_NAME: str
    DEBUG: bool

    class Config:
        env_file = ".env"

settings = Settings()
