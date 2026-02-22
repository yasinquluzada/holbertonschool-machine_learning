#!/usr/bin/env python3
"""2-precision module."""
import numpy as np


def precision(confusion):
    """Calculates the precision for each class."""
    confusion = np.asarray(confusion)
    true_pos = np.diag(confusion)
    predicted_pos = np.sum(confusion, axis=0)
    return np.where(predicted_pos == 0, 0.0, true_pos / predicted_pos)
