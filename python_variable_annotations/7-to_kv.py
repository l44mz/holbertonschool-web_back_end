#!/usr/bin/env python3
"""Module that provides a type-annotated key-value tuple function."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of the string k and the square of v as a float."""
    return (k, float(v ** 2))
