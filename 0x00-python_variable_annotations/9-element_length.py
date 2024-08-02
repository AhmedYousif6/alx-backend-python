#!/usr/bin/env python3
""" Duck type - iterable object """
from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ takes iterable sequence
    returns """
    return [(i, len(i)) for i in lst]
