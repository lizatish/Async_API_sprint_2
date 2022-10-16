import json
from typing import BinaryIO
from typing import List, Generator


def get_es_fw_bulk_query(es_data: List, es_index: str, es_id_field: str) -> Generator:
    """Генерирует документы для единовременной записи в es."""
    for doc in es_data:
        yield {
            '_op_type': 'index',
            '_id': doc[es_id_field],
            '_index': es_index,
            '_source': doc,
        }


def prepare_cache_output(redis_data_binary: BinaryIO) -> list[dict]:
    """Подготавливает результирующие данные, считанные из кеша."""
    redis_data = [json.loads(elem.decode()) for elem in redis_data_binary]
    return sorted(redis_data, key=lambda d: d['id'])


def prepare_expected_output(expected_answer: list[dict]) -> list[dict]:
    """Подготавливает результирующие эталонные данные для финальной проверки."""
    return sorted(expected_answer, key=lambda d: d['uuid'])


def compare_films_by_person_answer(prepared_cache_data: list[dict], sorted_expected_answer: list[dict]):
    """Сравнивает полученные и ожидаемые данные по фильмам, полученные из индекса персон."""
    for r_data, e_data in zip(prepared_cache_data, sorted_expected_answer):
        assert r_data['id'] == e_data['uuid']
        assert r_data['full_name'] == e_data['full_name']
        assert r_data['films'] == e_data['films']


def prepare_redis_film(film: bytes) -> dict:
    """Преобразует фильм из редиса к необходимому виду."""
    film = json.loads(film.decode())
    return {
        'uuid': film['id'],
        'title': film['title'],
        'imdb_rating': film['imdb_rating'],
    }
