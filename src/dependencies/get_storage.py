from src.storages import current_storage
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.storages.base import Storage


async def get_current_storage() -> 'Storage':
    return current_storage
