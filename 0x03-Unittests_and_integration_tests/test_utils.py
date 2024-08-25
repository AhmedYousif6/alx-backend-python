#!/usr/bin/env python3
""" task 0 module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Sequence, Mapping


class TestAccessNestedMap(unittest.TestCase):
    """ test class to test access nested
    map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """ test case or test unit
        test access nested map function with
        specific inputs.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
