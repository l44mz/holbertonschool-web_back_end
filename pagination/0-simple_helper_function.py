#!/usr/bin/env python3
"""
This module defines a simple helper function for pagination.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given pagination page.

    Given a 1-indexed page number and a page size, this function
    returns a tuple containing the start index and the end index
    that correspond to the range of items to display on that page
    of a list.

    Args:
        page: The 1-indexed page number to return.
        page_size: The number of items per page.

    Returns:
        A tuple of two integers (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
