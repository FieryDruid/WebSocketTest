from abc import ABC, abstractmethod
from typing import Any


class Storage(ABC):

    @property
    @abstractmethod
    async def data(self) -> dict[str, int | dict[str, str]]:
        """Словарь с сохранёнными данными"""
        raise NotImplementedError

    @abstractmethod
    async def set_data(self, value: Any) -> None:
        """Сеттер должен корректно сохранить данные, чтобы геттер их успешно отдал"""
        raise NotImplementedError
