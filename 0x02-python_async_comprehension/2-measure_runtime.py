#!/usr/bin/env python3
""" task 2 module """
import asyncio
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ return the time of execution async_comprehension """
    start_time = time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    total_time = time() - start_time
    return total_time
