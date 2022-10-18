import pytest
from aioredis import Redis
from httpx import AsyncClient

from tests.functional.config import get_settings
from tests.functional.testdata.films import (test_data_for_film_successful,
                                             test_data_for_film_unsuccessful,
                                             test_data_for_films_filter_nested_successful,
                                             test_data_for_films_filter_nested_unsuccessful,
                                             test_data_for_films_filter_simple_successful,
                                             test_data_for_films_filter_simple_unsuccessful,
                                             test_data_for_films_pagination_successful,
                                             test_data_for_films_pagination_unsuccessful,
                                             test_data_for_films_search_successful,
                                             test_data_for_films_search_unsuccessful,
                                             test_data_for_films_sort_successful,
                                             test_data_for_films_sort_unsuccessful)
from tests.functional.utils.helpers import prepare_redis_film, check_nested_filteres, check_simple_filteres

conf = get_settings()
pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize(
    'id_film, expected_body, expected_answer', test_data_for_film_successful
)
async def test_get_film_by_id_successful(
        film_works_api_client: AsyncClient, redis_pool: Redis, redis_flushall,
        id_film: str, expected_body: dict, expected_answer: dict
):
    """
    Тест для подробного просмотра film. Проверяет успешные запросы.

    Проверяет:
    - наличие фильма с указанным id
    - наличие фильма в кэше
    - соответствие фильма ожидаемому значению
    """
    response = await film_works_api_client.get(f'/api/v1/films/{id_film}')
    response_body = response.json()
    redis_film = prepare_redis_film(await redis_pool.get(id_film))

    assert redis_film['uuid'] == expected_body['uuid']
    assert redis_film['title'] == expected_body['title']
    assert redis_film['imdb_rating'] == expected_body['imdb_rating']
    assert response.status_code == expected_answer['status']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'id_film, expected_body, expected_answer', test_data_for_film_unsuccessful
)
async def test_get_film_by_id_unsuccessful(
        film_works_api_client: AsyncClient, redis_pool: Redis, redis_flushall,
        id_film: str, expected_body: dict, expected_answer: dict
):
    """
    Тест для подробного просмотра несуществующего film.

    Проверяет:
    - отсутствие фильма с указанным id
    - отсутствие фильма в кэше
    - соответствие тела ответа ожидаемому значению
    """
    response = await film_works_api_client.get(f'/api/v1/films/{id_film}')
    response_body = response.json()
    redis_data = await redis_pool.get(id_film)

    assert not redis_data
    assert response.status_code == expected_answer['status']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'query_param, expected_answer, expected_body', test_data_for_films_pagination_successful
)
async def test_films_pagination_successful(
        film_works_api_client: AsyncClient, redis_pool: Redis,
        redis_flushall, expected_body: list[dict], expected_answer: dict, query_param: str
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
    films = [prepare_redis_film(film) for film in redis_data]

    assert films[::-1] == expected_body
    assert len(redis_data) == expected_answer['redis_length']
    assert response.status_code == expected_answer['status']
    assert len(response_body) == expected_answer['response_length']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'query_param, expected_answer, expected_body', test_data_for_films_pagination_unsuccessful
)
async def test_films_pagination_unsuccessful(
        film_works_api_client: AsyncClient, redis_pool: Redis,
        redis_flushall, expected_body: dict, expected_answer: dict, query_param: str
):
    """
    Тест для невалидных параметров пагинации.

    Проверяет:
    - отсутствие фильмов в кэше
    - количество элементов в ответе на запрос
    - отсутствие элементов в кэше
    """
    response = await film_works_api_client.get(f'/api/v1/films/{query_param}')
    response_body = response.json()
    redis_data = await redis_pool.lrange(f'{conf.BASE_URL}/api/v1/films/{query_param}', 0, -1)

    assert not redis_data
    assert response.status_code == expected_answer['status']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'query_param, expected_answer, expected_body', test_data_for_films_sort_successful
)
async def test_films_sort_successful(
        film_works_api_client: AsyncClient, redis_pool: Redis,
        redis_flushall, expected_body: list[dict], expected_answer: dict, query_param: str
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
    films = [prepare_redis_film(film) for film in redis_data]
    is_first_item_is_greater_than_the_last = response_body[0]['imdb_rating'] >= response_body[-1]['imdb_rating']

    assert films[::-1] == expected_body
    assert len(redis_data) == expected_answer['redis_length']
    assert is_first_item_is_greater_than_the_last == expected_answer['is_first_item_is_greater_than_the_last']
    assert response.status_code == expected_answer['status']
    assert len(response_body) == expected_answer['response_length']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'query_param, expected_answer, expected_body', test_data_for_films_sort_unsuccessful
)
async def test_films_sort_unsuccessful(
        film_works_api_client: AsyncClient, redis_pool: Redis,
        redis_flushall, expected_body: list[dict], expected_answer: dict, query_param: str
):
    """
    Тест невалидных параметров сортировки.

    Проверяет:
    - отсутствие фильмов в кэше
    - количество элементов в ответе на запрос
    """
    response = await film_works_api_client.get(f'/api/v1/films/{query_param}')
    response_body = response.json()
    redis_data = await redis_pool.lrange(f'{conf.BASE_URL}/api/v1/films/{query_param}', 0, -1)

    assert not redis_data
    assert response.status_code == expected_answer['status']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'filter_name, query_param, expected_answer, expected_body', test_data_for_films_filter_nested_successful
)
async def test_films_filter_nested_successful(
        film_works_api_client: AsyncClient, redis_pool: Redis,
        redis_flushall, expected_body: list[dict], expected_answer: dict, query_param: str, filter_name: dict
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
    films = [prepare_redis_film(film) for film in redis_data]
    check_filter = check_nested_filteres(redis_data, filter_name)

    assert check_filter
    assert films[::-1] == expected_body
    assert len(redis_data) == expected_answer['redis_length']
    assert response.status_code == expected_answer['status']
    assert len(response_body) == expected_answer['response_length']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'query_param, expected_answer, expected_body', test_data_for_films_filter_nested_unsuccessful
)
async def test_films_filter_nested_unsuccessful(
        film_works_api_client: AsyncClient, redis_pool: Redis,
        redis_flushall, expected_body: list[dict], expected_answer: dict, query_param: str,
):
    """
    Тест на корректную работу при передаче несуществующих значений фильтров.

    Проверяет:
    - отсутствие фильмов в кэше
    - тело ответа ровно ожидаемому
    """
    response = await film_works_api_client.get(f'/api/v1/films/{query_param}')
    response_body = response.json()
    redis_data = await redis_pool.lrange(f'{conf.BASE_URL}/api/v1/films/{query_param}', 0, -1)

    assert not redis_data
    assert response.status_code == expected_answer['status']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'filter_name, query_param, expected_answer, expected_body', test_data_for_films_filter_simple_successful
)
async def test_films_filter_simple_successful(
        film_works_api_client: AsyncClient, redis_pool: Redis,
        redis_flushall, expected_body: list[dict], expected_answer: dict, query_param: str, filter_name: dict
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
    films = [prepare_redis_film(film) for film in redis_data]
    check_filter = check_simple_filteres(redis_data, filter_name)

    assert check_filter
    assert films[::-1] == expected_body
    assert len(redis_data) == expected_answer['redis_length']
    assert response.status_code == expected_answer['status']
    assert len(response_body) == expected_answer['response_length']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'query_param, expected_answer, expected_body', test_data_for_films_filter_simple_unsuccessful
)
async def test_films_filter_simple_unsuccessful(
        film_works_api_client: AsyncClient, redis_pool: Redis,
        redis_flushall, expected_body: dict, expected_answer: dict, query_param: str,
):
    """
    Тест на корректную работу при передаче несуществующих значений фильтров.

    Проверяет:
    - отсутствие фильмов в кэше
    - тело ответа ровно ожидаемому
    """
    response = await film_works_api_client.get(f'/api/v1/films/{query_param}')
    response_body = response.json()
    redis_data = await redis_pool.lrange(f'{conf.BASE_URL}/api/v1/films/{query_param}', 0, -1)

    assert not redis_data
    assert response.status_code == expected_answer['status']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'query_param, expected_answer, expected_body', test_data_for_films_search_successful
)
async def test_films_search_successful(
        film_works_api_client: AsyncClient, redis_pool: Redis,
        redis_flushall, expected_answer: dict, query_param: str, expected_body: list[dict]
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
    films = [prepare_redis_film(film) for film in redis_data]

    assert films[::-1] == expected_body
    assert len(redis_data) == expected_answer['redis_length']
    assert response.status_code == expected_answer['status']
    assert len(response_body) == expected_answer['response_length']
    assert response_body == expected_body


@pytest.mark.parametrize(
    'query_param, expected_answer, expected_body', test_data_for_films_search_unsuccessful
)
async def test_films_search_unsuccessful(
        film_works_api_client: AsyncClient, redis_pool: Redis,
        redis_flushall, expected_answer: dict, query_param: str, expected_body: list[dict]
):
    """
    Тест на корректную работу при передаче неверных параметров поиска.

    Проверяет:
    - отсутствие фильмов в кэше
    - тело ответа ровно ожидаемому
    """
    response = await film_works_api_client.get(f'/api/v1/films/search{query_param}')
    response_body = response.json()
    redis_data = await redis_pool.lrange(f'{conf.BASE_URL}/api/v1/films/search{query_param}', 0, -1)

    assert not redis_data
    assert response.status_code == expected_answer['status']
    assert response_body == expected_body
