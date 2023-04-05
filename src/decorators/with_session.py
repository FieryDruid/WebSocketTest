from collections.abc import Callable
from functools import wraps
from typing import Any

from aiohttp import ClientSession


def with_session(func: Callable) -> Callable:
    """Декоратор позволяет прокинуть объект сессии aiohttp в функцию"""
    @wraps(func)
    async def decorator(**kwargs) -> Any:
        async with ClientSession() as session:
            return await func(session=session, **kwargs)

    return decorator
