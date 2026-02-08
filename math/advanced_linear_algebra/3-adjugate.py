#!/usr/bin/env python3
"""Adjugate matrix computation."""


def _validate_matrix(matrix):
    """Validate that matrix is a non-empty square list of lists."""
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")


def _determinant(matrix):
    """Compute determinant of a square matrix (list of lists)."""
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    det = 0
    first_row = matrix[0]
    for j in range(n):
        if j % 2 == 0:
            sign = 1
        else:
            sign = -1
        minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += sign * first_row[j] * _determinant(minor)

    return det


def adjugate(matrix):
    """Calculate the adjugate matrix of a matrix."""
    _validate_matrix(matrix)

    n = len(matrix)
    if n == 1:
        return [[1]]

    cofactors = []
    for i in range(n):
        row_cof = []
        for j in range(n):
            minor = []
            for r in range(n):
                if r == i:
                    continue
                minor_row = []
                for c in range(n):
                    if c == j:
                        continue
                    minor_row.append(matrix[r][c])
                minor.append(minor_row)

            if (i + j) % 2 == 0:
                sign = 1
            else:
                sign = -1
            row_cof.append(sign * _determinant(minor))
        cofactors.append(row_cof)

    return [[cofactors[r][c] for r in range(n)] for c in range(n)]
