#!/usr/bin/env python3
"""Creates a confusion matrix for one-hot classification outputs."""

import numpy as np


def create_confusion_matrix(labels, logits):
    """Creates a confusion matrix from one-hot labels and predictions.

    Args:
        labels (np.ndarray): One-hot array of shape (m, classes) of true labels.
        logits (np.ndarray): One-hot array of shape (m, classes) of predictions.

    Returns:
        np.ndarray: Confusion matrix of shape (classes, classes).
        Rows are true classes; columns are predicted classes.
    """
    true_idx = np.argmax(labels, axis=1)
    pred_idx = np.argmax(logits, axis=1)
    classes = labels.shape[1]
    confusion = np.zeros((classes, classes), dtype=np.float64)
    np.add.at(confusion, (true_idx, pred_idx), 1)
    return confusion
