from db.redis import AsyncCacheStorage


class RedisService:
    def __init__(self, storage: AsyncCacheStorage):
        self.db = storage

    async def get(self, key: str) -> str:
        return await self.db.get(key)

    async def set(self, key: str, value: str, expire: int) -> str:
        return await self.db.set(key, value, expire=expire)

    async def lrange(self, key: str, start: int, stop: int) -> list:
        return await self.db.lrange(key, start=start, stop=stop)

    async def lpush(self, key: str, *elements: list[str]) -> int:
        return await self.db.lpush(key, *elements)

    async def expire(self, key: str, seconds: int) -> bool:
        return await self.db.expire(key, seconds)
