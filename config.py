import logging
import os
from functools import lru_cache

from pydantic_settings import BaseSettings

log = logging.getLogger('uvicorn')

class Settings(BaseSettings):
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: str = os.environ.get("DB_PORT")
    DB_SCHEMA: str = os.environ.get("DB_SCHEMA")

@lru_cache
def get_settings() -> BaseSettings:
    log.info("--- Loading the config settings from the environement ---")
    return Settings()