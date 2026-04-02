#!/usr/bin/env python3
"""Decision tree module using the Gini split criterion."""

import importlib.util
from pathlib import Path

import numpy as np


def _load_previous_module():
    """Load the most recent previous decision tree module."""
    current_dir = Path(__file__).resolve().parent
    for number in range(7, -1, -1):
        candidate = current_dir / f"{number}-build_decision_tree.py"
        if candidate.exists():
            module_name = f"build_{number}_decision_tree"
            spec = importlib.util.spec_from_file_location(
                module_name,
                candidate,
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
    raise FileNotFoundError("No previous decision tree module found.")


_previous_module = _load_previous_module()

Node = _previous_module.Node
Leaf = _previous_module.Leaf
Decision_Tree = _previous_module.Decision_Tree


def _possible_thresholds(self, node, feature):
    """Return all possible thresholds for one feature."""
    values = np.unique((self.explanatory[:, feature])[node.sub_population])
    return (values[1:] + values[:-1]) / 2


def _Gini_split_criterion_one_feature(self, node, feature):
    """Return the best threshold and Gini score for one feature."""
    thresholds = self.possible_thresholds(node, feature)
    if thresholds.size == 0:
        return 0.0, np.inf

    feature_values = self.explanatory[node.sub_population, feature]
    target_values = self.target[node.sub_population]
    classes = np.unique(target_values)

    class_filter = target_values[:, None] == classes[None, :]
    left_filter = feature_values[:, None] > thresholds[None, :]

    left_counts = (
        left_filter[:, :, None] & class_filter[:, None, :]
    ).sum(axis=0)
    total_counts = class_filter.sum(axis=0, keepdims=True)
    right_counts = total_counts - left_counts

    left_sizes = left_counts.sum(axis=1)
    right_sizes = right_counts.sum(axis=1)

    left_probs = np.divide(
        left_counts,
        left_sizes[:, None],
        out=np.zeros(left_counts.shape, dtype=float),
        where=left_sizes[:, None] != 0,
    )
    right_probs = np.divide(
        right_counts,
        right_sizes[:, None],
        out=np.zeros(right_counts.shape, dtype=float),
        where=right_sizes[:, None] != 0,
    )

    left_gini = 1 - np.sum(left_probs ** 2, axis=1)
    right_gini = 1 - np.sum(right_probs ** 2, axis=1)

    population_size = target_values.size
    gini_split = (
        (left_sizes / population_size) * left_gini
        + (right_sizes / population_size) * right_gini
    )

    best_index = np.argmin(gini_split)
    return thresholds[best_index], gini_split[best_index]


def _Gini_split_criterion(self, node):
    """Return the best feature and threshold using Gini impurity."""
    values = np.array(
        [
            self.Gini_split_criterion_one_feature(node, index)
            for index in range(self.explanatory.shape[1])
        ]
    )
    best_index = np.argmin(values[:, 1])
    return best_index, values[best_index, 0]


Decision_Tree.possible_thresholds = _possible_thresholds
Decision_Tree.Gini_split_criterion_one_feature = (
    _Gini_split_criterion_one_feature
)
Decision_Tree.Gini_split_criterion = _Gini_split_criterion
