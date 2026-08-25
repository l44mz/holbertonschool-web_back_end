#!/usr/bin/env python3
"""Module that provides an async comprehension coroutine."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from async_generator using async for."""
    return [i async for i in async_generator()]
