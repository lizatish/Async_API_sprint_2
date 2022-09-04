import time

from elasticsearch import AsyncElasticsearch

from tests.functional.config import get_settings

conf = get_settings()


def connect_es():
    """Ожидает подключения к es."""
    es_client = AsyncElasticsearch(hosts=[f'http://{conf.ELASTIC_HOST}:{conf.ELASTIC_PORT}'])
    while True:
        if es_client.ping():
            break
        time.sleep(1)


if __name__ == '__main__':
    connect_es()
