#!/usr/bin/env python3
"""Element-wise numpy-style operations without loops or conditionals."""


def np_elementwise(mat1, mat2):
    """Return (sum, difference, product, quotient) element-wise."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
