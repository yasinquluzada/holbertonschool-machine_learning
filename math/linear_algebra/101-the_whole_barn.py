#!/usr/bin/env python3
"""Matrix addition for any-dimensional nested Python lists."""


def add_matrices(mat1, mat2):
    """Add two matrices and return a new matrix or None if shapes differ."""
    is_list1 = isinstance(mat1, list)
    is_list2 = isinstance(mat2, list)

    if is_list1 != is_list2:
        return None

    if not is_list1:
        return mat1 + mat2

    if len(mat1) != len(mat2):
        return None

    result = []
    for item1, item2 in zip(mat1, mat2):
        summed = add_matrices(item1, item2)
        if summed is None:
            return None
        result.append(summed)
    return result
