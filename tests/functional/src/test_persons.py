import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_person_by_id(persons_api_client: AsyncClient):
    response = await persons_api_client.get("/api/v1/persons/d1507689-c396-4603-89ed-825022d64296")

    assert response.status_code == 200
