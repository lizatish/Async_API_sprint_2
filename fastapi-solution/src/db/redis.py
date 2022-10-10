from typing import Optional

from aioredis import Redis

cache: Optional[Redis] = None


# Функция понадобится при внедрении зависимостей
async def get_redis() -> Redis:
    """Возвращает экземпляр redis."""
    return cache
