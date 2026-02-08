#!/usr/bin/env python3
"""Matrix inverse computation module."""


def inverse(matrix):
    """Calculate the inverse of a square matrix.

    Args:
        matrix (list of lists): Matrix to invert.

    Returns:
        list of lists: The inverse of matrix, or None if matrix is singular.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a non-empty square matrix.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")
    if any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    aug = []
    for i, row in enumerate(matrix):
        left = [float(x) for x in row]
        right = [0.0] * n
        right[i] = 1.0
        aug.append(left + right)

    eps = 1e-12
    width = 2 * n

    for col in range(n):
        pivot_row = col
        pivot_val = abs(aug[col][col])
        for r in range(col + 1, n):
            val = abs(aug[r][col])
            if val > pivot_val:
                pivot_val = val
                pivot_row = r

        if pivot_val < eps:
            return None

        if pivot_row != col:
            aug[col], aug[pivot_row] = aug[pivot_row], aug[col]

        pivot = aug[col][col]
        for c in range(width):
            aug[col][c] /= pivot

        for r in range(n):
            if r != col:
                factor = aug[r][col]
                if abs(factor) > eps:
                    for c in range(width):
                        aug[r][c] -= factor * aug[col][c]

    return [row[n:] for row in aug]
