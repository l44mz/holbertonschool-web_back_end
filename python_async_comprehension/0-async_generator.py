#!/usr/bin/env python3
"""Module that provides an asynchronous generator coroutine."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield 10 random numbers between 0 and 10, waiting 1s each time."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
