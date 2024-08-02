#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ takes float number
    returns function that multiply float by multiplier param
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
