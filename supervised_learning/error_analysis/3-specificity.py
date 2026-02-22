#!/usr/bin/env python3
"""Module for calculating specificity per class from a confusion matrix."""
import numpy as np


def specificity(confusion):
    """Calculate specificity for each class in a confusion matrix.

    Args:
        confusion: numpy.ndarray (classes, classes). Rows are true labels and
            columns are predicted labels.

    Returns:
        numpy.ndarray (classes,) with specificity per class.
    """
    confusion = np.asarray(confusion)
    total = np.sum(confusion)

    tp = np.diag(confusion)
    fp = np.sum(confusion, axis=0) - tp
    fn = np.sum(confusion, axis=1) - tp
    tn = total - (tp + fp + fn)

    denom = tn + fp
    return np.where(denom == 0, 0.0, tn / denom)
