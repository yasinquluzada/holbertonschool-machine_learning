#!/usr/bin/env python3
"""Matrix concatenation along a specified axis for nested Python lists."""


def cat_matrices(mat1, mat2, axis=0):
    """Concatenate two matrices along axis; return new matrix or None."""
    if not isinstance(axis, int) or axis < 0:
        return None

    if _shape(mat1) != _shape(mat2):
        if axis == 0:
            if not _same_structure_except_axis(mat1, mat2, axis):
                return None
            return _cat_axis0(mat1, mat2)
        if not _can_cat(mat1, mat2, axis):
            return None
        return _cat(mat1, mat2, axis)

    if not _can_cat(mat1, mat2, axis):
        return None
    return _cat(mat1, mat2, axis)


def _shape(mat):
    """Return the shape of a nested list structure."""
    shp = []
    cur = mat
    while isinstance(cur, list):
        shp.append(len(cur))
        if len(cur) == 0:
            break
        cur = cur[0]
    return tuple(shp)


def _can_cat(mat1, mat2, axis):
    """Check if concatenation is possible along the given axis."""
    s1 = _shape(mat1)
    s2 = _shape(mat2)

    if len(s1) != len(s2):
        return False
    if axis >= len(s1):
        return False

    for i in range(len(s1)):
        if i == axis:
            continue
        if s1[i] != s2[i]:
            return False
    return _same_depth(mat1, mat2)


def _same_depth(a, b):
    """Ensure both operands are lists/leaves at the same nesting depth."""
    a_is_list = isinstance(a, list)
    b_is_list = isinstance(b, list)
    if a_is_list != b_is_list:
        return False
    if not a_is_list:
        return True
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if not _same_depth(x, y):
            return False
    return True


def _cat(mat1, mat2, axis):
    """Concatenate two matrices along axis assuming it is valid."""
    if axis == 0:
        return _cat_axis0(mat1, mat2)
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    out = []
    for a, b in zip(mat1, mat2):
        c = _cat(a, b, axis - 1)
        if c is None:
            return None
        out.append(c)
    return out


def _cat_axis0(mat1, mat2):
    """Concatenate along axis 0 by copying elements."""
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None
    out = []
    for item in mat1:
        out.append(_deep_copy(item))
    for item in mat2:
        out.append(_deep_copy(item))
    return out


def _deep_copy(x):
    """Deep copy nested lists (no imports)."""
    if isinstance(x, list):
        return [_deep_copy(v) for v in x]
    return x


def _same_structure_except_axis(mat1, mat2, axis):
    """Compatibility helper for axis 0 shape mismatch."""
    return _can_cat(mat1, mat2, axis)
