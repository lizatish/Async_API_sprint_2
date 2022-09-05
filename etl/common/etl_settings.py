import os

from pydantic import BaseSettings


class ETLSettings(BaseSettings):
    """Настройки приложения."""

    POSTGRES_DB_NAME: str
    POSTGRES_DB_USER: str
    POSTGRES_DB_PASSWORD: str
    POSTGRES_DB_HOST: str = 'postgres'
    POSTGRES_DB_PORT: int = 5432

    DATA_BATCH_SIZE: int = 50

    ELASTIC_HOST: str = 'elastic'
    ELASTIC_PORT: int = 9200

    PATH_TO_STORAGE_JSON: str = 'storage.json'

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    class Config:
        """Дополнительные базовые настройки."""

        env_file = '.env'
        env_file_encoding = 'utf-8'
