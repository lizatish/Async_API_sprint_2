import asyncio
import logging

import aioredis

from tests.functional.config import get_settings
from tests.functional.logger import get_logger
from tests.functional.utils.connection import backoff

conf = get_settings()
logger = get_logger()
backoff_logger = logging.getLogger(__name__)


@backoff(
    Exception,
    backoff_logger=logger,
)
async def connect_redis():
    """Ожидание подключения к redis"""
    redis_client = await aioredis.create_redis_pool(
        (conf.CACHE_HOST, conf.CACHE_PORT), minsize=10, maxsize=20, encoding='utf-8',
    )
    logger.debug('Connection established!')
    redis_client.close()


if __name__ == '__main__':
    asyncio.run(connect_redis())
