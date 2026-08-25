#!/usr/bin/env python3
"""Module that provides a type-annotated element length function."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples pairing each element with its length."""
    return [(i, len(i)) for i in lst]
