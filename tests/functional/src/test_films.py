import json

import pytest
from aioredis import Redis
from httpx import AsyncClient
from tests.functional.config import get_settings
from tests.functional.testdata.films import (test_data_for_film,
                                             test_data_for_films_filter_nested,
                                             test_data_for_films_filter_simple,
                                             test_data_for_films_pagination,
                                             test_data_for_films_search,
                                             test_data_for_films_sort)

conf = get_settings()


@pytest.mark.parametrize(
    'id_film, expected_body, expected_answer', test_data_for_film
)
@pytest.mark.asyncio
async def test_get_film_by_id(
    film_works_api_client: AsyncClient, redis_pool: Redis, id_film: str, expected_body: dict, expected_answer: dict
):
    """
    Тест для подробного просмотра film.

    Проверяет:
    - наличие фильма с указанным id
    - наличие фильма в кэше
    - соответствие фильма ожидаемому значению
    """
    response = await film_works_api_client.get(f'/api/v1/films/{id_film}')
    response_body = response.json()
    redis_data = await redis_pool.get(id_film)
    if expected_answer['redis_data']:
        assert redis_data
    else:
        assert not redis_data
    assert response.status_code == expected_answer['status']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'query_param, expected_answer', test_data_for_films_pagination
)
@pytest.mark.asyncio
async def test_films_pagination(
    film_works_api_client: AsyncClient, redis_pool: Redis, expected_answer: dict, query_param: str
):
    """
    Тест на корректную работу пагинации при запросе к films.

    Проверяет:
    - наличие фильмов в кэше
    - количество элементов в ответе на запрос
    - количество элементов в кэше
    """
    response = await film_works_api_client.get(f'/api/v1/films/{query_param}')
    response_body = response.json()
    redis_data = await redis_pool.lrange(f'{conf.BASE_URL}/api/v1/films/{query_param}', 0, -1)
    if expected_answer['redis_data']:
        assert redis_data
    else:
        assert not redis_data
    assert len(redis_data) == expected_answer['redis_length']
    assert response.status_code == expected_answer['status']
    assert len(response_body) == expected_answer['response_length']


@pytest.mark.parametrize(
    'query_param, expected_answer', test_data_for_films_sort
)
@pytest.mark.asyncio
async def test_films_sort(
    film_works_api_client: AsyncClient, redis_pool: Redis, expected_answer: dict, query_param: str
):
    """
    Тест на корректную работу сортировки при запросе к films.

    Проверяет:
    - наличие фильмов в кэше
    - количество элементов в ответе на запрос
    - количество элементов в кэше
    - что первый элемент больше или меньше последнего (в зависимости от типа сортировки)
    """
    response = await film_works_api_client.get(f'/api/v1/films/{query_param}')
    response_body = response.json()
    redis_data = await redis_pool.lrange(f'{conf.BASE_URL}/api/v1/films/{query_param}', 0, -1)
    if expected_answer['redis_data']:
        assert redis_data
    else:
        assert not redis_data
    if expected_answer['comparison'] == 0:
        assert response_body[0]['imdb_rating'] >= response_body[-1]['imdb_rating']
    elif expected_answer['comparison'] == 1:
        assert response_body[0]['imdb_rating'] <= response_body[-1]['imdb_rating']
    assert len(redis_data) == expected_answer['redis_length']
    assert response.status_code == expected_answer['status']
    assert len(response_body) == expected_answer['response_length']


@pytest.mark.parametrize(
    'filter_name, query_param, expected_answer', test_data_for_films_filter_nested
)
@pytest.mark.asyncio
async def test_films_filter_nested(
    film_works_api_client: AsyncClient, redis_pool: Redis, expected_answer: dict, query_param: str, filter_name: dict
):
    """
    Тест на корректную работу вложенных фильтров при запросе к films.

    Проверяет:
    - наличие фильмов в кэше
    - количество элементов в ответе на запрос
    - количество элементов в кэше
    - что указанный в фильтре id присутствует в ответе
    """
    response = await film_works_api_client.get(f'/api/v1/films/{query_param}')
    response_body = response.json()
    redis_data = await redis_pool.lrange(f'{conf.BASE_URL}/api/v1/films/{query_param}', 0, -1)
    if expected_answer['redis_data']:
        assert redis_data
        if filter_name:
            for item in redis_data:
                for filter_ in filter_name:
                    data = json.loads(item.decode('utf-8'))
                    tmp = [i['id'] for i in data[filter_]]
                    assert filter_name[filter_] in tmp
    else:
        assert not redis_data
    assert len(redis_data) == expected_answer['redis_length']
    assert response.status_code == expected_answer['status']
    assert len(response_body) == expected_answer['response_length']


@pytest.mark.parametrize(
    'filter_name, query_param, expected_answer', test_data_for_films_filter_simple
)
@pytest.mark.asyncio
async def test_films_filter_simple(
    film_works_api_client: AsyncClient, redis_pool: Redis, expected_answer: dict, query_param: str, filter_name: dict
):
    """
    Тест на корректную работу простых фильтров при запросе к films.

    Проверяет:
    - наличие фильмов в кэше
    - количество элементов в ответе на запрос
    - количество элементов в кэше
    - что указанное значение фильтра присутствует в ответе
    """
    response = await film_works_api_client.get(f'/api/v1/films/{query_param}')
    response_body = response.json()
    redis_data = await redis_pool.lrange(f'{conf.BASE_URL}/api/v1/films/{query_param}', 0, -1)
    if expected_answer['redis_data']:
        assert redis_data
        if filter_name:
            for item in redis_data:
                for filter_ in filter_name:
                    data = json.loads(item.decode('utf-8'))
                    assert str(filter_name[filter_]) in str(data[filter_]) or filter_name[filter_] == data[filter_]
    else:
        assert not redis_data
    assert len(redis_data) == expected_answer['redis_length']
    assert response.status_code == expected_answer['status']
    assert len(response_body) == expected_answer['response_length']


@pytest.mark.parametrize(
    'query_param, expected_answer', test_data_for_films_search
)
@pytest.mark.asyncio
async def test_films_search(
    film_works_api_client: AsyncClient, redis_pool: Redis, expected_answer: dict, query_param: str
):
    """
    Тест на корректную поиска при запросе к films/search.

    Проверяет:
    - наличие фильмов в кэше
    - количество элементов в ответе на запрос
    - количество элементов в кэше
    """
    response = await film_works_api_client.get(f'/api/v1/films/search{query_param}')
    response_body = response.json()
    redis_data = await redis_pool.lrange(f'{conf.BASE_URL}/api/v1/films/search{query_param}', 0, -1)
    if expected_answer['redis_data']:
        assert redis_data
    else:
        assert not redis_data
    assert len(redis_data) == expected_answer['redis_length']
    assert response.status_code == expected_answer['status']
    assert len(response_body) == expected_answer['response_length']
