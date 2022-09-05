import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_film_by_id(film_works_api_client: AsyncClient):
    response = await film_works_api_client.get("/api/v1/films/db594b91-a587-48c4-bac9-5c6be5e4cf33")

    assert response.status_code == 200
