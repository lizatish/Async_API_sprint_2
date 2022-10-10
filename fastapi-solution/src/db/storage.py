from abc import ABC, abstractmethod


class AsyncCacheStorage(ABC):
    """Абстрактный класс для кеша."""

    @abstractmethod
    async def get(self, key: str, **kwargs) -> str:
        """Возвращает элементы по ключу.

         Args:
            key: ключ
            kwargs: доп. параметры

        Returns:
            str: элементы по ключу
        """
        pass

    @abstractmethod
    async def set(self, key: str, value: str, expire: int, **kwargs) -> str:
        """Записывает ключ для хранения значения.

         Args:
            key: ключ
            value: значение
            expire: время актуальности данных
            kwargs: доп. параметры

        Returns:
            str: строковое представление результата операции
        """
        pass

    @abstractmethod
    async def lrange(self, key: str, start: int, stop: int, **kwargs) -> list:
        """Возвращает диапазон значений, лежащих по ключу.

        Args:
            key: ключ
            start: начальное смещение
            stop: конечное смещение
            kwargs: доп. параметры

        Returns:
            list: список элементов, попавших в диапазон
        """
        pass

    @abstractmethod
    async def lpush(self, key: str, element: str, **kwargs) -> int:
        """Кладет элемент в список по ключу в начало очереди.

        Args:
            key: ключ
            element: значение элемента
            kwargs: доп. параметры

        Returns:
            int: размер списка по ключу после вставки
        """
        pass

    @abstractmethod
    async def expire(self, key: str, seconds: int, **kwargs) -> bool:
        """Задает время, после которого ключ станет невалидным.

        Args:
            key: ключ
            seconds: количество секунд
            kwargs: доп. параметры

         Returns:
            bool: результат выполнения операции
        """
        pass


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
