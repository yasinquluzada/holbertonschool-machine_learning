#!/usr/bin/env python3
"""5-definiteness module."""


import numpy as np


def definiteness(matrix):
    """Calculate the definiteness of a matrix.

    Args:
        matrix (numpy.ndarray): Array of shape (n, n).

    Returns:
        str or None: One of:
            "Positive definite", "Positive semi-definite",
            "Negative semi-definite", "Negative definite",
            "Indefinite", or None for invalid matrices.

    Raises:
        TypeError: If matrix is not a numpy.ndarray.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.ndim != 2:
        return None

    n, m = matrix.shape
    if n == 0 or n != m:
        return None

    if not np.all(np.isfinite(matrix)):
        return None

    if not np.allclose(matrix, matrix.T):
        return None

    vals = np.linalg.eigvalsh(matrix)

    tol = 1e-10
    pos = np.all(vals > tol)
    pos_semi = np.all(vals >= -tol) and np.any(np.abs(vals) <= tol)
    neg = np.all(vals < -tol)
    neg_semi = np.all(vals <= tol) and np.any(np.abs(vals) <= tol)

    if pos:
        return "Positive definite"
    if pos_semi:
        return "Positive semi-definite"
    if neg:
        return "Negative definite"
    if neg_semi:
        return "Negative semi-definite"
    if np.any(vals > tol) and np.any(vals < -tol):
        return "Indefinite"

    return None
