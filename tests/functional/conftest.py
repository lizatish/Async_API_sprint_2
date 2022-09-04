import asyncio
from typing import List, AsyncIterator

import pytest
import pytest_asyncio
from aioredis import create_redis_pool, Redis
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk
from fastapi.testclient import TestClient
from httpx import AsyncClient

from db import elastic
from db import redis
from main import app
from tests.functional.config import get_settings
from tests.functional.testdata.es_mapping import es_film_works_data
from tests.functional.utils.elastic import get_es_fw_bulk_query

conf = get_settings()


@pytest.fixture
def es_write_data(es_client):
    async def inner(data: List[dict]):
        await async_bulk(
            es_client,
            get_es_fw_bulk_query(
                data,
                conf.ELASTIC_INDEX,
                conf.ELASTIC_ID_FIELD_NAME,
            ),
        )

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
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def film_works_es_writer(es_write_data):
    await es_write_data(es_film_works_data)


@pytest.fixture
def api_client(event_loop, es_client, redis_pool) -> TestClient:
    elastic.es = es_client
    redis.redis = redis_pool
    client = AsyncClient(app=app, base_url="http://localhost")
    yield client
    event_loop.run_until_complete(client.aclose())


@pytest_asyncio.fixture
async def film_works_api_client(api_client, film_works_es_writer):
    await film_works_es_writer
    yield api_client
