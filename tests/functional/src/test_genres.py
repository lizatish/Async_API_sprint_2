import pytest
from aioredis import Redis
from httpx import AsyncClient
from tests.functional.config import get_settings
from tests.functional.testdata.genres import (test_data_for_genre,
                                              test_data_for_genres_list)

conf = get_settings()


@pytest.mark.parametrize(
    'id_genre, expected_body, expected_answer', test_data_for_genre
)
@pytest.mark.asyncio
async def test_get_genre_by_id(
    film_works_api_client: AsyncClient, redis_pool: Redis, id_genre: str, expected_body: dict, expected_answer: dict
):
    """
    Тест для подробного просмотра genre.

    Проверяет:
    - наличие жанра с указанным id
    - наличие жанра в кэше
    - соответствие жанра ожидаемому значению
    """
    response = await film_works_api_client.get(f'/api/v1/genres/{id_genre}')
    response_body = response.json()
    redis_data = await redis_pool.get(id_genre)
    assert (False if redis_data is None else True) == expected_answer['redis_data']
    assert response.status_code == expected_answer['status']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'expected_answer', test_data_for_genres_list
)
@pytest.mark.asyncio
async def test_get_genres_list(
    film_works_api_client: AsyncClient, redis_pool: Redis, expected_answer: dict
):
    """
    Тест для получения всех жанров.

    Проверяет:
    - наличие жанров в кэше
    - количество элементов в ответе на запрос
    - количество элементов в кэше
    """
    response = await film_works_api_client.get(f'/api/v1/genres/')
    response_body = response.json()
    redis_data = await redis_pool.lrange(f'{conf.BASE_URL}/api/v1/genres/', 0, -1)
    assert (False if redis_data is None else True) == expected_answer['redis_data']
    assert len(redis_data) == expected_answer['redis_length']
    assert response.status_code == expected_answer['status']
    assert len(response_body) == expected_answer['response_length']
