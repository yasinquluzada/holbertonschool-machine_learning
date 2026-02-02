#!/usr/bin/env python3
"""2D matrix concatenation along a specified axis (0 or 1)."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate two 2D matrices along axis; return new matrix or None."""
    if axis not in (0, 1):
        return None
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None
    if len(mat1) == 0 or len(mat2) == 0:
        return None
    if not _is_2d(mat1) or not _is_2d(mat2):
        return None

    r1 = len(mat1)
    c1 = len(mat1[0])
    r2 = len(mat2)
    c2 = len(mat2[0])

    if axis == 0:
        if c1 != c2:
            return None
        out = []
        for row in mat1:
            out.append(row[:])
        for row in mat2:
            out.append(row[:])
        return out

    if r1 != r2:
        return None
    out = []
    for i in range(r1):
        out.append(mat1[i][:] + mat2[i][:])
    return out


def _is_2d(mat):
    """Check matrix is a non-empty 2D list with consistent row lengths."""
    if not isinstance(mat, list) or len(mat) == 0:
        return False
    if not isinstance(mat[0], list):
        return False
    cols = len(mat[0])
    for row in mat:
        if not isinstance(row, list):
            return False
        if len(row) != cols:
            return False
    return True
