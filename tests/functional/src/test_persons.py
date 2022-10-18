import pytest
from aioredis import Redis
from httpx import AsyncClient
from http import HTTPStatus

from tests.functional.config import get_settings
from tests.functional.testdata.persons import (test_data_for_persons_pagination,
                                               test_data_search_persons,
                                               test_data_get_films_by_person_successful,
                                               test_data_get_films_by_person_unsuccessful,
                                               test_data_get_film_by_id_successful,
                                               test_data_get_film_by_id_unsuccessful)
from tests.functional.utils.helpers import prepare_redis_person, prepare_redis_film

conf = get_settings()
pytestmark = pytest.mark.asyncio


async def test_validate_search_persons(persons_api_client: AsyncClient, redis_flushall):
    not_validated_size_field_params_first = {'size': 'hjj', 'query': 'Mark'}
    not_validated_number_field_params_second = {'number': 'hjj', 'query': 'Mark'}

    first_response = await persons_api_client.get('/api/v1/persons/search', params=not_validated_size_field_params_first)
    second_response = await persons_api_client.get('/api/v1/persons/search', params=not_validated_number_field_params_second)

    assert first_response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert second_response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


@pytest.mark.parametrize(
    'person_id, expected_answer, expected_status', test_data_get_film_by_id_successful
)
async def test_get_person_by_id_successful(persons_api_client: AsyncClient, redis_pool: Redis, redis_flushall, person_id: str,
                                expected_answer: dict, expected_status: int):
    response = await persons_api_client.get(f'/api/v1/persons/{person_id}')
    body = response.json()
    redis_person = prepare_redis_person(await redis_pool.get(f"enriched_{person_id}"))

    assert redis_person['uuid'] == expected_answer['uuid']
    assert redis_person['full_name'] == expected_answer['full_name']
    assert redis_person['films'] == expected_answer['films']
    assert response.status_code == expected_status
    assert body == expected_answer


@pytest.mark.parametrize(
    'person_id, expected_answer, expected_status', test_data_get_film_by_id_unsuccessful
)
async def test_get_person_by_id_unsuccessful(persons_api_client: AsyncClient, redis_pool: Redis, redis_flushall, person_id: str,
                                expected_answer: dict, expected_status: int):
    response = await persons_api_client.get(f'/api/v1/persons/{person_id}')
    body = response.json()
    redis_person = await redis_pool.get(f"enriched_{person_id}")

    assert not redis_person
    assert response.status_code == expected_status
    assert body == expected_answer


@pytest.mark.parametrize(
    'person_id, expected_answer, expected_status', test_data_get_films_by_person_successful
)
async def test_get_films_by_person_successful(persons_api_client: AsyncClient, redis_pool: Redis, redis_flushall, person_id: str,
                                   expected_answer: list[dict], expected_status: int):
    response = await persons_api_client.get(f'/api/v1/persons/{person_id}/film')
    body = response.json()
    cache_data_binary = await redis_pool.lrange(f'film_by_person_{person_id}', 0, -1)
    films = [prepare_redis_film(film) for film in cache_data_binary]

    assert films[::-1] == expected_answer
    assert response.status_code == expected_status
    assert body == expected_answer


@pytest.mark.parametrize(
    'person_id, expected_answer, expected_status', test_data_get_films_by_person_unsuccessful
)
async def test_get_films_by_person_unsuccessful(persons_api_client: AsyncClient, redis_pool: Redis, redis_flushall, person_id: str,
                                   expected_answer: list[dict], expected_status: int):
    response = await persons_api_client.get(f'/api/v1/persons/{person_id}/film')
    body = response.json()
    cache_data_binary = await redis_pool.lrange(f'film_by_person_{person_id}', 0, -1)

    assert not cache_data_binary
    assert response.status_code == expected_status
    assert body == expected_answer


@pytest.mark.parametrize(
    'query, expected_answer', test_data_search_persons
)
async def test_search_persons(persons_api_client: AsyncClient, redis_pool: Redis, redis_flushall, query: str,
                              expected_answer: list[dict]):
    url = f'/api/v1/persons/search{query}'

    response = await persons_api_client.get(url)
    body = response.json()
    cache_data_binary = await redis_pool.lrange(f"enriched_{conf.BASE_URL}{url}", 0, -1)
    persons = [prepare_redis_person(person) for person in cache_data_binary]

    assert persons[::-1] == expected_answer
    assert response.status_code == HTTPStatus.OK
    assert body == expected_answer


@pytest.mark.parametrize(
    'query, expected_answer', test_data_for_persons_pagination
)
async def test_pagination_persons(
        persons_api_client: AsyncClient,
        redis_flushall,
        redis_pool: Redis,
        query: str,
        expected_answer: list[dict]
):
    url = f'/api/v1/persons/search{query}'

    response = await persons_api_client.get(url)
    body = response.json()
    cache_data_binary = await redis_pool.lrange(f"enriched_{conf.BASE_URL}{url}", 0, -1)
    persons = [prepare_redis_person(person) for person in cache_data_binary]

    assert persons[::-1] == expected_answer
    assert response.status_code == HTTPStatus.OK
    assert body == expected_answer
