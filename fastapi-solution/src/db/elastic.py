from abc import ABC, abstractmethod
from typing import Optional


class AsyncSearchEngine(ABC):
    """Абстрактный класс, реализующий работу поискового движка."""

    @abstractmethod
    def __init__(self, **kwargs):
        """Инициализирует поисковой движок."""
        pass

    @abstractmethod
    async def close(self, **kwargs):
        """Закрывает соединение с движком.."""
        pass

    @abstractmethod
    async def search(
            self,
            index: str,
            from_: int = None,
            size: int = None,
            body: dict = None,
            **kwargs,
    ):
        """Производит поиск документов."""
        pass

    @abstractmethod
    async def get(self, index: str, id: str, **kwargs) -> dict:
        """Возвращает документ заданного индекса по идентификатору."""
        pass


es: Optional[AsyncSearchEngine] = None


# Функция понадобится при внедрении зависимостей
async def get_elastic_storage() -> AsyncSearchEngine:
    """Возвращает экземпляр es."""
    return es
