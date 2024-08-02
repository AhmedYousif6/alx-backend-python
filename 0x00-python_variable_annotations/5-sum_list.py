#!/usr/bin/env python3
""" Complex types - List of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ takes list of floats and returns the sum (float) """
    sum_float = 0
    for x in input_list:
        sum_float += x
    return sum_float
