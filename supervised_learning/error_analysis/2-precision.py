#!/usr/bin/env python3
"""Per-class precision from a confusion matrix."""
import numpy as np


def precision(confusion):
    """Calculates the precision for each class in a confusion matrix.

    Args:
        confusion (np.ndarray): Shape (classes, classes). Rows are true labels
            and columns are predicted labels.

    Returns:
        np.ndarray: Shape (classes,) containing precision for each class.
    """
    confusion = np.asarray(confusion)
    tp = np.diag(confusion)
    predicted = np.sum(confusion, axis=0)
    return np.divide(tp, predicted, out=np.zeros_like(tp, dtype=float),
                     where=predicted != 0)
