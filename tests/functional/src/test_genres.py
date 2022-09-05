import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_genres_list(genres_api_client: AsyncClient):
    response = await genres_api_client.get("/api/v1/genres/")

    assert response.status_code == 200
