#!/usr/bin/env python3
"""
An asychronous coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """takes in an integer argument &
        waits for a random delay
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
