#!/usr/bin/env python3
"""Module that provides a type-annotated multiplier factory function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiplier_fn(n: float) -> float:
        """Multiply the given float by the enclosing multiplier."""
        return n * multiplier
    return multiplier_fn
