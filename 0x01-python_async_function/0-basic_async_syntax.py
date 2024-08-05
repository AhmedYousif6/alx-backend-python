#!/usr/bin/env python3

""" The basics of async """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchorouns coroutine takes an integer with default value of 10
    and delay in range of (0 - max_delay)
    return that delay time
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
