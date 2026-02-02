#!/usr/bin/env python3
"""NumPy matrix concatenation along a specified axis."""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two matrices along a specific axis and return a new array."""
    return np.concatenate((mat1, mat2), axis=axis)
