import asyncio
import json
from asyncio import AbstractEventLoop
from typing import AsyncIterator, Callable

import aioredis
import pytest
import pytest_asyncio
from aioredis import Redis
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk
from httpx import AsyncClient

from db import elastic
from db import redis
from db.elastic import AsyncSearchEngine
from main import app
from tests.functional.config import get_settings
from tests.functional.testdata.films import es_film_works_data
from tests.functional.testdata.genres import es_genres_data
from tests.functional.testdata.persons import es_persons_data
from tests.functional.utils.helpers import get_es_fw_bulk_query

conf = get_settings()


async def create_index(es, index_name, index_json_path):
    """Создает индекс в случае его отсутствия."""
    if not await es.indices.exists(index=index_name):
        with open(index_json_path, 'r') as index_file:
            index_dict = json.load(index_file)
            await es.indices.create(
                index=index_name,
                ignore=400,
                **index_dict,
            )


@pytest_asyncio.fixture(scope="session")
async def es_write_data(es_client: AsyncElasticsearch) -> Callable:
    """Фикстура записи данных в es."""

    async def inner(data: list[dict], es_index: str, index_json_path: str):
        """Внутренний метод для записи списка данных одним запросом в es."""
        await create_index(es_client, es_index, index_json_path)
        await async_bulk(
            es_client,
            get_es_fw_bulk_query(
                data,
                es_index,
                conf.SEARCH_ENGINE_ID_FIELD_NAME,
            ),
        )

    return inner


@pytest_asyncio.fixture(scope="session")
async def es_client() -> AsyncSearchEngine:
    """Фикстура соединения с es."""
    client = AsyncElasticsearch(hosts=[f'http://{conf.SEARCH_ENGINE_HOST}:{conf.SEARCH_ENGINE_PORT}'])
    yield client
    await client.close()


@pytest_asyncio.fixture(scope="session")
async def redis_pool() -> AsyncIterator[Redis]:
    """Фикстура соединения с redis."""
    pool = aioredis.from_url(
        f"redis://{conf.CACHE_HOST}:{conf.CACHE_PORT}", encoding="utf-8", decode_responses=True
    )
    yield pool
    await pool.close()


@pytest_asyncio.fixture
async def redis_flushall(redis_pool):
    """Фикстура, удаляющая кеш редиса."""
    await redis_pool.flushall()


@pytest.fixture(scope="session")
def event_loop() -> AbstractEventLoop:
    """Фикстура главного цикла событий."""
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def api_client(event_loop: AbstractEventLoop, es_client: AsyncElasticsearch, redis_pool: Redis) -> AsyncClient:
    """Фикстура апи-клиента с моком es и redis."""
    elastic.es = es_client
    redis.cache = redis_pool
    client = AsyncClient(app=app, base_url=conf.BASE_URL)
    yield client
    event_loop.run_until_complete(client.aclose())


@pytest_asyncio.fixture(scope="session")
async def film_works_api_client(api_client: AsyncClient, es_write_data: Callable) -> AsyncClient:
    """Фикстура апи-клиента с заполненными данными es для тестирования фильмов."""
    await es_write_data(es_film_works_data, conf.SEARCH_ENGINE_FILM_WORKS_INDEX,
                        conf.SEARCH_ENGINE_FILM_WORKS_INDEX_FILE)
    yield api_client


@pytest_asyncio.fixture(scope="session")
async def persons_api_client(
        api_client: AsyncClient,
        es_write_data: Callable,
        film_works_api_client: AsyncClient,
) -> AsyncClient:
    """Фикстура апи-клиента с заполненными данными es для тестирования участников фильма."""
    await es_write_data(es_persons_data, conf.SEARCH_ENGINE_PERSONS_INDEX, conf.SEARCH_ENGINE_PERSONS_INDEX_FILE)
    yield api_client


@pytest_asyncio.fixture(scope="session")
async def genres_api_client(api_client: AsyncClient, es_write_data: Callable) -> AsyncClient:
    """Фикстура апи-клиента с заполненными данными es для тестирования жанров."""
    await es_write_data(es_genres_data, conf.SEARCH_ENGINE_GENRES_INDEX, conf.SEARCH_ENGINE_GENRES_INDEX_FILE)
    yield api_client
