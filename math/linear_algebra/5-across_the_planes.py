#!/usr/bin/env python3
"""Element-wise addition for two 2D matrices represented as Python lists."""


def add_matrices2D(mat1, mat2):
    """Add two 2D matrices element-wise; return new matrix or None."""
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None
    if len(mat1) != len(mat2):
        return None
    if len(mat1) == 0:
        return None

    result = []
    for row1, row2 in zip(mat1, mat2):
        if not isinstance(row1, list) or not isinstance(row2, list):
            return None
        if len(row1) != len(row2):
            return None
        new_row = []
        for a, b in zip(row1, row2):
            new_row.append(a + b)
        result.append(new_row)
    return result
