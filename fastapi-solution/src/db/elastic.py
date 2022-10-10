from typing import Optional

from db.storage import AsyncSearchEngine

es: Optional[AsyncSearchEngine] = None


# Функция понадобится при внедрении зависимостей
async def get_elastic() -> AsyncSearchEngine:
    """Возвращает экземпляр es."""
    return es
