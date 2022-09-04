import pytest
from fastapi.testclient import TestClient

from core.config import get_settings
from db import elastic, redis
from main import app
from tests.functional.config import get_settings as test_settings

client = TestClient(app)

app.dependency_overrides[get_settings] = test_settings



@pytest.mark.asyncio
async def test_index(client, es_client, redis_pool):
    elastic.es = es_client
    redis.redis = redis_pool

    print(redis.redis)
    print(elastic.es)

    response = await client.get("/api/v1/genres")
    assert response.status_code == 200
    print(response.status_code)
