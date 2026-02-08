#!/usr/bin/env python3
"""Minor matrix module.

Defines a function to compute the minor matrix of a square matrix.
"""


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
    for j, value in enumerate(matrix[0]):
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        sign = -1 if j % 2 else 1
        det += sign * value * _determinant(sub)
    return det


def minor(matrix):
    """Calculate the minor matrix of a square matrix."""
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError('matrix must be a list of lists')
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a list of lists')

    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError('matrix must be a non-empty square matrix')

    if n == 1:
        return [[1]]

    minors = []
    for i in range(n):
        row_minors = []
        for j in range(n):
            sub = []
            for r in range(n):
                if r == i:
                    continue
                sub.append(matrix[r][:j] + matrix[r][j + 1:])
            row_minors.append(_determinant(sub))
        minors.append(row_minors)
    return minors
