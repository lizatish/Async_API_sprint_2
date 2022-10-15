import json

import pytest
from aioredis import Redis
from httpx import AsyncClient

from tests.functional.config import get_settings
from tests.functional.testdata.persons import test_data_for_persons_pagination, test_data_search_persons, \
    test_data_get_films_by_person, test_data_get_film_by_id
from tests.functional.utils.helpers import prepare_cache_output, prepare_expected_output, compare_films_by_person_answer

conf = get_settings()


@pytest.mark.asyncio
async def test_validate_search_persons(persons_api_client: AsyncClient, redis_flushall):
    not_validated_size_field_params = {'size': 'hjj', 'query': 'Mark'}
    response = await persons_api_client.get('/api/v1/persons/search', params=not_validated_size_field_params)
    assert response.status_code == 422

    not_validated_number_field_params = {'number': 'hjj', 'query': 'Mark'}
    response = await persons_api_client.get('/api/v1/persons/search', params=not_validated_number_field_params)
    assert response.status_code == 422


@pytest.mark.parametrize(
    'person_id, expected_answer, expected_status, is_use_cache', test_data_get_film_by_id
)
@pytest.mark.asyncio
async def test_get_person_by_id(persons_api_client: AsyncClient, redis_pool: Redis, redis_flushall, person_id: str,
                                expected_answer: dict, expected_status: int, is_use_cache: bool):
    response = await persons_api_client.get(f'/api/v1/persons/{person_id}')
    assert response.status_code == expected_status
    body = response.json()
    assert body == expected_answer

    if is_use_cache:
        cache_data_binary = await redis_pool.get(person_id)
        cache_data = json.loads(cache_data_binary.decode())
        compare_films_by_person_answer([cache_data], [expected_answer])


@pytest.mark.parametrize(
    'person_id, expected_answer, expected_status, is_use_cache', test_data_get_films_by_person
)
@pytest.mark.asyncio
async def test_get_films_by_person(persons_api_client: AsyncClient, redis_pool: Redis, redis_flushall, person_id: str,
                                   expected_answer: list[dict], expected_status: int, is_use_cache: bool):
    response = await persons_api_client.get(f'/api/v1/persons/{person_id}/film')
    assert response.status_code == expected_status
    body = response.json()
    assert body == expected_answer
    if is_use_cache:
        cache_data_binary = await redis_pool.lrange(f'film_by_person_{person_id}', 0, -1)
        prepared_cache_data = prepare_cache_output(cache_data_binary)
        prepared_expected_answer = prepare_expected_output(expected_answer)
        for r_data, e_data in zip(prepared_cache_data, prepared_expected_answer):
            assert r_data['id'] == e_data['uuid']
            assert r_data['title'] == e_data['title']
            assert r_data['imdb_rating'] == e_data['imdb_rating']


@pytest.mark.parametrize(
    'query, expected_answer, is_use_cache', test_data_search_persons
)
@pytest.mark.asyncio
async def test_search_persons(persons_api_client: AsyncClient, redis_pool: Redis, redis_flushall, query: str,
                              expected_answer: list[dict], is_use_cache: bool):
    url = f'/api/v1/persons/search{query}'
    response = await persons_api_client.get(url)
    assert response.status_code == 200
    body = response.json()
    assert body == expected_answer

    if is_use_cache:
        cache_data_binary = await redis_pool.lrange(f"{conf.BASE_URL}{url}", 0, -1)
        prepared_cache_data = prepare_cache_output(cache_data_binary)
        prepared_expected_answer = prepare_expected_output(expected_answer)
        compare_films_by_person_answer(prepared_cache_data, prepared_expected_answer)


@pytest.mark.parametrize(
    'query, expected_answer, is_use_cache', test_data_for_persons_pagination
)
@pytest.mark.asyncio
async def test_pagination_persons(
        persons_api_client: AsyncClient,
        redis_flushall,
        redis_pool: Redis,
        query: str,
        expected_answer: list[dict],
        is_use_cache: bool
):
    url = f'/api/v1/persons/search{query}'
    response = await persons_api_client.get(url)
    assert response.status_code == 200

    if is_use_cache:
        cache_data_binary = await redis_pool.lrange(f"{conf.BASE_URL}{url}", 0, -1)
        prepared_cache_data = prepare_cache_output(cache_data_binary)
        prepared_expected_answer = prepare_expected_output(expected_answer)
        compare_films_by_person_answer(prepared_cache_data, prepared_expected_answer)
