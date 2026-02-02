#!/usr/bin/env python3
"""2D matrix multiplication for matrices of ints/floats."""


def mat_mul(mat1, mat2):
    """Multiply two 2D matrices; return new matrix or None if impossible."""
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None
    if len(mat1) == 0 or len(mat2) == 0:
        return None
    if not _is_matrix(mat1) or not _is_matrix(mat2):
        return None

    rows_a = len(mat1)
    cols_a = len(mat1[0])
    rows_b = len(mat2)
    cols_b = len(mat2[0])

    if cols_a != rows_b:
        return None

    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            s = 0
            for k in range(cols_a):
                s += mat1[i][k] * mat2[k][j]
            row.append(s)
        result.append(row)
    return result


def _is_matrix(mat):
    """Validate a 2D matrix structure (rectangular, non-empty rows)."""
    if not isinstance(mat, list) or len(mat) == 0:
        return False
    if not isinstance(mat[0], list) or len(mat[0]) == 0:
        return False
    row_len = len(mat[0])
    for row in mat:
        if not isinstance(row, list) or len(row) != row_len:
            return False
    return True
