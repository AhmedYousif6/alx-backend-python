#!/usr/bin/env python3
""" Duck type - advanced task """
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ takes an argument (any)
    returns the first element if its not None
    otherwise returns None"""
    if lst:
        return lst[0]
    else:
        return None
