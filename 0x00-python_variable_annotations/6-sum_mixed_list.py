#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ takes list of ints and floats and returns the sum (float) """
    sum_float = 0
    for x in mxd_lst:
        sum_float += x
    return sum_float
