import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Настройки приложения."""

    # Название проекта. Используется в Swagger-документации
    PROJECT_NAME: str = 'movies'

    # Настройки Redis
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379

    # Настройки Elasticsearch
    ELASTIC_HOST: str = 'localhost'
    ELASTIC_PORT: int = 9200
    ELASTIC_INDEX: str = 'movies'
    ELASTIC_ID_FIELD_NAME: str = 'id'

    # Корень проекта
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_URL: str = 'http://localhost'

    # Время хранения данных в кэше
    FILM_CACHE_EXPIRE_IN_SECONDS: int = 60 * 5
    GENRE_CACHE_EXPIRE_IN_SECONDS: int = 60 * 5
    PERSON_CACHE_EXPIRE_IN_SECONDS: int = 60 * 5

    class Config:
        """Дополнительные базовые настройки."""

        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    """Возвращает настройки тестов."""
    return Settings()
