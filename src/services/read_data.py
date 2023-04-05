from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.storages.base import Storage


async def read_data(storage: 'Storage') -> dict[str, int | dict[str, str]]:
    return await storage.data
