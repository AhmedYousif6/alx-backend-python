#!/usr/bin/env python3
""" More involved type annotations - advanced task """
from typing import Union, Any, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """ takes dict and key
    returns the key of the dict or None if key not in the dict
    """
    if key in dct:
        return dct[key]
    else:
        return default
