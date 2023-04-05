import time
from asyncio import Lock

from src.storages.base import Storage


class InMemoryStorage(Storage):
    __slots__ = ('_data', 'lock')

    def __init__(self):
        self._data = {}
        self.lock = Lock()

    @property
    async def data(self) -> dict[str, int | dict[str, str]]:
        return self._data

    async def set_data(self, value: dict) -> None:
        async with self.lock:
            self._data = {'timestamp': int(time.time()), 'data': value}
