#!/usr/bin/env python3
"""
An async routine
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ takes in 2 int arguments (in this order): n and max_delay.
        You will spawn wait_random n times with the specified max_delay
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return sorted(delays)
