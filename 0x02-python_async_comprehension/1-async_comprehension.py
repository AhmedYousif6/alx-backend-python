#!/usr/bin/env python3
""" task 1 module """
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ collect 10 values from async generator """
    lis = [value async for value in async_generator()]
    return lis
