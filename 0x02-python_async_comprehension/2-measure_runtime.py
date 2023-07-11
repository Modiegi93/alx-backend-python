#!/usr/bin/env python3
"""
Async gather
"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure runtime"""
    start_time = time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time()
    total_runtime = end_time - start_time

    return total_runtime
