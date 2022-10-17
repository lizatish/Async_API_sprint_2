from elasticsearch import NotFoundError

from core.config import get_settings
from db.elastic import AsyncSearchEngine

conf = get_settings()


class ElasticService:
    def __init__(self, storage: AsyncSearchEngine, es_index: str):
        self.db = storage
        self.es_index = es_index

    async def search(self,
                     from_: int = None,
                     size: int = conf.ELASTIC_DEFAULT_OUTPUT_RECORDS_SIZE,
                     query: dict = None,
                     sort: str = None,
                     ):
        try:
            doc = await self.db.search(
                index=self.es_index,
                from_=from_,
                size=size,
                query=query,
                sort=sort,
            )
        except NotFoundError:
            return None
        return doc['hits']['hits']

    async def get(self, doc_id: str):
        try:
            doc = await self.db.get(index=self.es_index, id=doc_id)
        except NotFoundError:
            return None
        return doc
