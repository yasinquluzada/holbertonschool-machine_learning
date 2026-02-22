#!/usr/bin/env python3
"""1-sensitivity module."""
import numpy as np


def sensitivity(confusion):
    """Calculates the sensitivity (recall) for each class."""
    confusion = np.asarray(confusion)
    true_pos = np.diag(confusion)
    possible_pos = np.sum(confusion, axis=1)
    return np.where(possible_pos == 0, 0.0, true_pos / possible_pos)
