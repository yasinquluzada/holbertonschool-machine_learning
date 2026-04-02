#!/usr/bin/env python3
"""Isolation random tree module."""

import numpy as np

Node = __import__("8-build_decision_tree").Node
Leaf = __import__("8-build_decision_tree").Leaf


class Isolation_Random_Tree:
    """Isolation random tree."""

    def __init__(self, max_depth=10, seed=0, root=None):
        """Initialize an isolation random tree."""
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.max_depth = max_depth
        self.predict = None
        self.min_pop = 1

    def __str__(self):
        """Return the string representation of the tree."""
        return self.root.__str__()

    def depth(self):
        """Return the maximum depth of the tree."""
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """Count the nodes or the leaves of the tree."""
        return self._count_nodes_below(self.root, only_leaves)

    def _count_nodes_below(self, node, only_leaves=False):
        """Count the nodes or the leaves below a node."""
        if node is None:
            return 0
        if node.is_leaf:
            return 1
        if only_leaves:
            return (
                self._count_nodes_below(node.left_child, True)
                + self._count_nodes_below(node.right_child, True)
            )
        return (
            1
            + self._count_nodes_below(node.left_child, False)
            + self._count_nodes_below(node.right_child, False)
        )

    def update_bounds(self):
        """Update the bounds of the tree when available."""
        if hasattr(self.root, "update_bounds_below"):
            self.root.update_bounds_below()

    def get_leaves(self):
        """Return the leaves of the tree."""
        leaves = []
        self._get_leaves_below(self.root, leaves)
        return leaves

    def _get_leaves_below(self, node, leaves):
        """Append the leaves below a node to a list."""
        if node is None:
            return
        if node.is_leaf:
            leaves.append(node)
            return
        self._get_leaves_below(node.left_child, leaves)
        self._get_leaves_below(node.right_child, leaves)

    def update_predict(self):
        """Update the prediction function of the tree."""
        self.predict = lambda arr: np.array(
            [self._predict_one(self.root, row) for row in arr]
        )

    def _predict_one(self, node, row):
        """Predict the value for a single row."""
        if node.is_leaf:
            return node.value
        if row[node.feature] > node.threshold:
            return self._predict_one(node.left_child, row)
        return self._predict_one(node.right_child, row)

    def np_extrema(self, arr):
        """Return the minimum and maximum of an array."""
        return np.min(arr), np.max(arr)

    def random_split_criterion(self, node):
        """Choose a random valid split for a node."""
        valid_features = []
        for feature in range(self.explanatory.shape[1]):
            values = self.explanatory[node.sub_population, feature]
            lower, upper = self.np_extrema(values)
            if lower < upper:
                valid_features.append((feature, lower, upper))

        if not valid_features:
            return 0, 0

        index = self.rng.integers(0, len(valid_features))
        feature, lower, upper = valid_features[index]
        threshold = self.rng.uniform(lower, upper)
        return feature, threshold

    def get_leaf_child(self, node, sub_population):
        """Create a leaf child for a node."""
        leaf_child = Leaf(node.depth + 1)
        leaf_child.depth = node.depth + 1
        leaf_child.sub_population = sub_population
        return leaf_child

    def get_node_child(self, node, sub_population):
        """Create an internal child node for a node."""
        node_child = Node()
        node_child.depth = node.depth + 1
        node_child.sub_population = sub_population
        return node_child

    def _is_leaf_population(self, sub_population, depth):
        """Tell whether a population must become a leaf."""
        if np.sum(sub_population) <= self.min_pop:
            return True
        if depth >= self.max_depth:
            return True
        subset = self.explanatory[sub_population]
        if subset.size == 0:
            return True
        return np.all(np.ptp(subset, axis=0) == 0)

    def fit_node(self, node):
        """Fit a node and its descendants."""
        node.feature, node.threshold = self.random_split_criterion(node)

        left_population = node.sub_population & (
            self.explanatory[:, node.feature] > node.threshold
        )
        right_population = node.sub_population & ~left_population

        is_left_leaf = self._is_leaf_population(
            left_population,
            node.depth + 1,
        )

        if is_left_leaf:
            node.left_child = self.get_leaf_child(node, left_population)
        else:
            node.left_child = self.get_node_child(node, left_population)
            self.fit_node(node.left_child)

        is_right_leaf = self._is_leaf_population(
            right_population,
            node.depth + 1,
        )

        if is_right_leaf:
            node.right_child = self.get_leaf_child(node, right_population)
        else:
            node.right_child = self.get_node_child(node, right_population)
            self.fit_node(node.right_child)

    def fit(self, explanatory, verbose=0):
        """Train the isolation random tree."""
        self.split_criterion = self.random_split_criterion
        self.explanatory = explanatory
        self.root.sub_population = np.ones(
            explanatory.shape[0],
            dtype=bool,
        )

        if self._is_leaf_population(self.root.sub_population, self.root.depth):
            self.root = Leaf(self.root.depth, depth=self.root.depth)
            self.root.is_root = True
            self.root.sub_population = np.ones(
                explanatory.shape[0],
                dtype=bool,
            )
        else:
            self.fit_node(self.root)

        self.update_predict()

        if verbose == 1:
            print(
                f"""  Training finished.
    - Depth                     : {self.depth()}
    - Number of nodes           : {self.count_nodes()}
    - Number of leaves          : {self.count_nodes(only_leaves=True)}"""
            )
        return self
