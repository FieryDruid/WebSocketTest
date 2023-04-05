from fastapi import APIRouter, WebSocket, Depends
import asyncio

from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError

from src.dependencies.get_storage import get_current_storage
from src.services.read_data import read_data
from src.storages.base import Storage

get_data_router = APIRouter()


@get_data_router.websocket('/test')
async def get_data(websocket: WebSocket, storage: Storage = Depends(get_current_storage)) -> None:
    await websocket.accept()
    while True:
        data = await read_data(storage)
        try:
            await websocket.send_json(data)
        except (ConnectionClosedOK, ConnectionClosedError):
            return
        await asyncio.sleep(1)
