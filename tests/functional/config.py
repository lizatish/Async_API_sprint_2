import logging
import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Настройки приложения."""

    # Название проекта. Используется в Swagger-документации
    PROJECT_NAME: str = 'movies'

    # Настройки логирования
    LOG_LEVEL: int = logging.DEBUG

    # Настройки Redis
    CACHE_HOST: str = 'localhost'
    CACHE_PORT: int = 6379

    # Корень проекта
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_URL: str = 'http://test-api_service'

    # Настройки поискового движка
    SEARCH_ENGINE_HOST: str = 'localhost'
    SEARCH_ENGINE_PORT: int = 9200
    SEARCH_ENGINE_FILM_WORKS_INDEX: str = 'movies'
    SEARCH_ENGINE_PERSONS_INDEX: str = 'persons'
    SEARCH_ENGINE_GENRES_INDEX: str = 'genres'
    SEARCH_ENGINE_ID_FIELD_NAME: str = 'id'
    SEARCH_ENGINE_GENRES_INDEX_FILE: str = BASE_DIR + '/functional/indices/genre.json'
    SEARCH_ENGINE_PERSONS_INDEX_FILE: str = BASE_DIR + '/functional/indices/persons.json'
    SEARCH_ENGINE_FILM_WORKS_INDEX_FILE: str = BASE_DIR + '/functional/indices/movies.json'

    # Время хранения данных в кэше
    FILM_CACHE_EXPIRE_IN_SECOND: int = 60 * 5
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
