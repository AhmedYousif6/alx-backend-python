#!/usr/bin/env python3
""" task 0 module """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ loops 10 times and generate every time random number
    between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
