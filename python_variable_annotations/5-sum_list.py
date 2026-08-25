#!/usr/bin/env python3
"""Module that provides a type-annotated function to sum a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all floats in the given list."""
    return sum(input_list)
