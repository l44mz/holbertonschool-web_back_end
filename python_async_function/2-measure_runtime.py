#!/usr/bin/env python3
"""Module that provides a function to measure wait_n's average runtime."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure total runtime of wait_n(n, max_delay) and return the average."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n
