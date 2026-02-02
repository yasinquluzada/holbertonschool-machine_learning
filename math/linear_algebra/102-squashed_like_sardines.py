#!/usr/bin/env python3
"""Matrix concatenation along a specified axis for nested Python lists."""


def cat_matrices(mat1, mat2, axis=0):
    """Concatenate two matrices along axis; return a new matrix or None."""
    if not isinstance(axis, int) or axis < 0:
        return None
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None
    if not _compatible(mat1, mat2, axis):
        return None
    return _concat(mat1, mat2, axis)


def _compatible(a, b, axis):
    """Return True if a and b can be concatenated along the given axis."""
    if not isinstance(a, list) or not isinstance(b, list):
        return False
    if axis == 0:
        return _same_subshape(a, b)
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if not _compatible(x, y, axis - 1):
            return False
    return True


def _same_subshape(a, b):
    """For axis=0, all dimensions except axis must match."""
    if len(a) == 0 or len(b) == 0:
        return False
    return _shape(a[0]) == _shape(b[0])


def _shape(x):
    """Return the shape tuple of a (well-formed) nested list structure."""
    if isinstance(x, list):
        if len(x) == 0:
            return (0,)
        return (len(x),) + _shape(x[0])
    return ()


def _concat(a, b, axis):
    """Concatenate a and b along axis (assumes compatibility)."""
    if axis == 0:
        left = [_deep_copy(v) for v in a]
        right = [_deep_copy(v) for v in b]
        return left + right
    out = []
    for x, y in zip(a, b):
        out.append(_concat(x, y, axis - 1))
    return out


def _deep_copy(x):
    """Deep copy nested lists without imports."""
    if isinstance(x, list):
        return [_deep_copy(v) for v in x]
    return x
