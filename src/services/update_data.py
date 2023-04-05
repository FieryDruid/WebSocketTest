import asyncio
from typing import TYPE_CHECKING

from aiohttp import ClientResponse, ClientSession

from src.decorators import with_session

if TYPE_CHECKING:
    from src.storages.base import Storage

SUCCESS = 200


@with_session
async def update_data(*, storage: 'Storage', timeout_sec: int = 5, session: ClientSession, **_) -> None:
    while True:
        async with session.get('https://blockchain.info/ticker') as response:
            response: ClientResponse
            if response.status != SUCCESS:
                continue
            response_data = await response.json()
            await storage.set_data(response_data.get('ARS', {}))
        await asyncio.sleep(timeout_sec)
