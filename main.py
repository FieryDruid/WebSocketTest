import asyncio

import uvicorn
from fastapi import FastAPI

from src.routes.get_data import get_data_router
from src.services.update_data import update_data
from src.dependencies.get_storage import get_current_storage

app = FastAPI(redoc_url=None)
app.include_router(get_data_router)

tasks = set()


@app.on_event('startup')
async def run_collect_data() -> None:
    task = asyncio.create_task(
        update_data(storage=await get_current_storage())
    )
    tasks.add(task)
    task.add_done_callback(tasks.discard)

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=9000,
        reload=True,
        log_level='info'
    )
