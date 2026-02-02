#!/usr/bin/env python3
"""Slice a NumPy ndarray along specified axes."""


def np_slice(matrix, axes={}):
    """Return a sliced copy of a NumPy ndarray using an axes spec."""
    slices = [slice(None)] * matrix.ndim
    for axis, slc in axes.items():
        slices[axis] = slice(*slc)
    return matrix[tuple(slices)].copy()
