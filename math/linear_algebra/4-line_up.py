#!/usr/bin/env python3
"""Element-wise addition for two same-length numeric arrays."""


def add_arrays(arr1, arr2):
    """Return a new list with element-wise sums, or None if shapes differ."""
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
