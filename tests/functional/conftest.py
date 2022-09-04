import asyncio
from typing import List, AsyncIterator

import pytest
import pytest_asyncio
from aioredis import create_redis_pool, Redis
from elasticsearch import AsyncElasticsearch
from httpx import AsyncClient

from main import app
from tests.functional.config import get_settings
from tests.functional.testdata.es_mapping import test_data_for_film_search
from tests.functional.utils.elastic import get_es_bulk_query

conf = get_settings()


@pytest.fixture
def es_write_data(es_client):
    async def inner(data: List[dict]):
        bulk_query = get_es_bulk_query(data, conf.es_index, conf.es_id_field)
        str_query = '\n'.join(bulk_query) + '\n'
        response = await es_client.bulk(str_query, refresh=True)
        if response['errors']:
            raise Exception('Ошибка записи данных в Elasticsearch')

    return inner


@pytest_asyncio.fixture
async def es_client():
    client = AsyncElasticsearch(hosts=[f'http://{conf.ELASTIC_HOST}:{conf.ELASTIC_PORT}'])
    yield client
    await client.close()


@pytest_asyncio.fixture
async def redis_pool() -> AsyncIterator[Redis]:
    pool = await create_redis_pool((conf.REDIS_HOST, conf.REDIS_PORT), minsize=10, maxsize=20)
    yield pool
    pool.close()
    await pool.wait_closed()


@pytest.fixture
def client(event_loop):
    client = AsyncClient(app=app, base_url="http://localhost")
    yield client
    event_loop.run_until_complete(client.aclose())


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="module")
def film_works_es_writer(es_write_data):
    await es_write_data(test_data_for_film_search)
