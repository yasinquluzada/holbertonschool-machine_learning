#!/usr/bin/env python3
"""Determinant calculation module."""


def determinant(matrix):
    """Calculate the determinant of a square matrix.

    Args:
        matrix (list of lists): Matrix to evaluate.

    Returns:
        int or float: Determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a square matrix.
    """
    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        return 1

    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if n == 1:
        return matrix[0][0]
    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    det = 0
    first_row = matrix[0]
    for col in range(n):
        minor = []
        for i in range(1, n):
            minor.append(matrix[i][:col] + matrix[i][col + 1:])
        sign = -1 if col % 2 else 1
        det += sign * first_row[col] * determinant(minor)
    return det
