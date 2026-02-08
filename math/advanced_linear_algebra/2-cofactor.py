#!/usr/bin/env python3
"""Cofactor matrix computation."""


def _validate_matrix(matrix):
    """Validate the input matrix for cofactor computation."""
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")


def _minor_matrix(matrix, row, col):
    """Return the minor matrix after removing one row and one column."""
    minor = []
    for i, r in enumerate(matrix):
        if i == row:
            continue
        new_row = []
        for j, val in enumerate(r):
            if j == col:
                continue
            new_row.append(val)
        minor.append(new_row)
    return minor


def _determinant(matrix):
    """Compute the determinant of a square matrix."""
    n = len(matrix)
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j, val in enumerate(matrix[0]):
        sign = -1 if j % 2 else 1
        det += sign * val * _determinant(_minor_matrix(matrix, 0, j))
    return det


def cofactor(matrix):
    """Calculate the cofactor matrix of a matrix.

    Args:
        matrix: list of lists whose cofactor matrix should be calculated

    Returns:
        The cofactor matrix of matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not a non-empty square matrix
    """
    _validate_matrix(matrix)
    n = len(matrix)
    if n == 1:
        return [[1]]
    cof = []
    for i in range(n):
        row = []
        for j in range(n):
            sign = -1 if (i + j) % 2 else 1
            row.append(sign * _determinant(_minor_matrix(matrix, i, j)))
        cof.append(row)
    return cof
