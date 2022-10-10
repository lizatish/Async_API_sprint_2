import asyncio

import elastic_transport
from elasticsearch import AsyncElasticsearch

from tests.functional.config import get_settings
from tests.functional.logger import get_logger
from tests.functional.utils.connection import backoff

conf = get_settings()
logger = get_logger()


@backoff(
    elastic_transport.ApiError,
    elastic_transport.TransportError,
    elastic_transport.ConnectionError,
    backoff_logger=logger,
)
async def connect_es():
    """Ожидает подключения к es."""
    es_client = AsyncElasticsearch(hosts=[f'http://{conf.ELASTIC_HOST}:{conf.ELASTIC_PORT}'])
    await es_client.perform_request('HEAD', '/')
    logger.debug('Connection established!')
    await es_client.close()


if __name__ == '__main__':
    asyncio.run(connect_es())
