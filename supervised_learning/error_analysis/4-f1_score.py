#!/usr/bin/env python3
"""4-f1_score module."""
import numpy as np

sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """Calculates the F1 score of each class in a confusion matrix."""
    prec = precision(confusion)
    sens = sensitivity(confusion)
    denom = prec + sens
    return np.where(denom == 0, 0.0, 2.0 * (prec * sens) / denom)
