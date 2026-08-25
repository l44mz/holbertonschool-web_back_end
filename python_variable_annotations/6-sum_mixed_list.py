#!/usr/bin/env python3
"""Module that provides a type-annotated function to sum a mixed list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list containing ints and floats, as a float."""
    return sum(mxd_lst)
