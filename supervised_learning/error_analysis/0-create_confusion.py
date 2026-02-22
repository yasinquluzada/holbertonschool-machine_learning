#!/usr/bin/env python3
"""Confusion matrix creation for one-hot classification outputs."""

import numpy as np


def create_confusion_matrix(labels, logits):
    """Create a confusion matrix from one-hot true/predicted labels.

    Args:
        labels (np.ndarray): Shape (m, classes). One-hot true labels.
        logits (np.ndarray): Shape (m, classes). One-hot predicted labels.

    Returns:
        np.ndarray: Shape (classes, classes). Rows are true classes and
        columns are predicted classes.
    """
    true_idx = np.argmax(labels, axis=1)
    pred_idx = np.argmax(logits, axis=1)
    classes = labels.shape[1]
    confusion = np.zeros((classes, classes), dtype=np.float64)
    np.add.at(confusion, (true_idx, pred_idx), 1)
    return confusion
