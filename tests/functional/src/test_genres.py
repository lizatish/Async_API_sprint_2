import pytest
from aioredis import Redis
from httpx import AsyncClient
from tests.functional.config import get_settings
from tests.functional.testdata.genres import (test_data_for_genre,
                                              test_data_for_genres_list)
from tests.functional.utils.helpers import prepare_redis_genre

conf = get_settings()


@pytest.mark.parametrize(
    'id_genre, expected_body, expected_answer', test_data_for_genre
)
@pytest.mark.asyncio
async def test_get_genre_by_id(
    genres_api_client: AsyncClient, redis_pool: Redis, redis_flushall,
    id_genre: str, expected_body: dict, expected_answer: dict
):
    """
    Тест для подробного просмотра genre.

    Проверяет:
    - наличие жанра с указанным id
    - наличие жанра в кэше
    - соответствие жанра ожидаемому значению
    """
    response = await genres_api_client.get(f'/api/v1/genres/{id_genre}')
    response_body = response.json()
    if expected_answer['redis_data']:
        redis_genre = prepare_redis_genre(await redis_pool.get(id_genre))
        assert redis_genre == expected_body
    assert response.status_code == expected_answer['status']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'expected_answer, expected_body', test_data_for_genres_list
)
@pytest.mark.asyncio
async def test_get_genres_list(
    genres_api_client: AsyncClient, redis_pool: Redis, redis_flushall,
    expected_answer: dict, expected_body: list
):
    """
    Тест для получения всех жанров.

    Проверяет:
    - наличие жанров в кэше
    - количество элементов в ответе на запрос
    - количество элементов в кэше
    """
    response = await genres_api_client.get(f'/api/v1/genres/')
    response_body = response.json()
    redis_data = await redis_pool.lrange(f'{conf.BASE_URL}/api/v1/genres/', 0, -1)
    if expected_answer['redis_data']:
        genres = [prepare_redis_genre(genre) for genre in redis_data]
        assert genres[::-1] == expected_body
    assert len(redis_data) == expected_answer['redis_length']
    assert response.status_code == expected_answer['status']
    assert len(response_body) == expected_answer['response_length']
    assert response_body == expected_body
