import asyncio
import time

import aioredis

from tests.functional.config import get_settings

conf = get_settings()


async def connect_redis():
    """Ожидание подключения к redis"""
    redis_client = await aioredis.create_redis_pool((conf.REDIS_HOST, conf.REDIS_PORT), minsize=10, maxsize=20)
    while True:
        if redis_client.ping():
            break
        time.sleep(1)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(connect_redis())
