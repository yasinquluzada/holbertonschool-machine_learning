#!/usr/bin/env python3
"""Decision tree training module."""

import numpy as np


class Node:
    """Decision tree internal node."""

    def __init__(
        self,
        feature=None,
        threshold=None,
        left_child=None,
        right_child=None,
        is_root=False,
        depth=0,
    ):
        """Initialize a decision tree node."""
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """Return the maximum depth found below this node."""
        depths = [self.depth]
        if self.left_child is not None:
            depths.append(self.left_child.max_depth_below())
        if self.right_child is not None:
            depths.append(self.right_child.max_depth_below())
        return max(depths)

    def count_nodes_below(self, only_leaves=False):
        """Count the nodes below this node."""
        count = 0 if only_leaves else 1
        if self.left_child is not None:
            count += self.left_child.count_nodes_below(only_leaves)
        if self.right_child is not None:
            count += self.right_child.count_nodes_below(only_leaves)
        return count

    def pred(self, x):
        """Predict the class for one sample."""
        if x[self.feature] > self.threshold:
            return self.left_child.pred(x)
        return self.right_child.pred(x)


class Leaf(Node):
    """Decision tree leaf."""

    def __init__(self, value, depth=None):
        """Initialize a decision tree leaf."""
        super().__init__(depth=depth)
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """Return the depth of the leaf."""
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """Count the leaf as one node."""
        return 1

    def pred(self, x):
        """Predict the stored class for one sample."""
        return self.value


class Decision_Tree:
    """Decision tree classifier."""

    def __init__(
        self,
        max_depth=10,
        min_pop=1,
        seed=0,
        split_criterion="random",
        root=None,
    ):
        """Initialize the decision tree."""
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """Return the maximum depth of the tree."""
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """Count nodes in the tree."""
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def update_predict(self):
        """Create the prediction function of the tree."""
        self.predict = lambda explanatory: np.array(
            [self.root.pred(row) for row in explanatory]
        )

    def np_extrema(self, arr):
        """Return the minimum and maximum of a numpy array."""
        return np.min(arr), np.max(arr)

    def random_split_criterion(self, node):
        """Choose a random split for a node."""
        diff = 0
        while diff == 0:
            feature = self.rng.integers(0, self.explanatory.shape[1])
            feature_min, feature_max = self.np_extrema(
                self.explanatory[:, feature][node.sub_population]
            )
            diff = feature_max - feature_min
        x = self.rng.uniform()
        threshold = (1 - x) * feature_min + x * feature_max
        return feature, threshold

    def Gini_split_criterion(self, node):
        """Use the random split until Gini is implemented later."""
        return self.random_split_criterion(node)

    def _is_leaf_population(self, sub_population, depth):
        """Check whether a child population must become a leaf."""
        if np.sum(sub_population) < self.min_pop:
            return True
        if depth == self.max_depth:
            return True
        return np.unique(self.target[sub_population]).size == 1

    def get_leaf_child(self, node, sub_population):
        """Create a leaf child from a sub-population."""
        values, counts = np.unique(
            self.target[sub_population], return_counts=True
        )
        value = values[np.argmax(counts)]
        leaf_child = Leaf(value, depth=node.depth + 1)
        leaf_child.sub_population = sub_population
        return leaf_child

    def get_node_child(self, node, sub_population):
        """Create an internal child node from a sub-population."""
        child = Node(depth=node.depth + 1)
        child.sub_population = sub_population
        return child

    def fit_node(self, node):
        """Recursively train the subtree rooted at a node."""
        node.feature, node.threshold = self.split_criterion(node)
        feature_values = self.explanatory[:, node.feature]
        left_population = np.logical_and(
            node.sub_population,
            feature_values > node.threshold,
        )
        right_population = np.logical_and(
            node.sub_population,
            feature_values <= node.threshold,
        )
        child_depth = node.depth + 1
        is_left_leaf = self._is_leaf_population(left_population, child_depth)
        if is_left_leaf:
            node.left_child = self.get_leaf_child(node, left_population)
        else:
            node.left_child = self.get_node_child(node, left_population)
            self.fit_node(node.left_child)
        is_right_leaf = self._is_leaf_population(right_population, child_depth)
        if is_right_leaf:
            node.right_child = self.get_leaf_child(node, right_population)
        else:
            node.right_child = self.get_node_child(node, right_population)
            self.fit_node(node.right_child)

    def fit(self, explanatory, target, verbose=0):
        """Train the decision tree on a dataset."""
        if self.split_criterion == "random":
            self.split_criterion = self.random_split_criterion
        else:
            self.split_criterion = self.Gini_split_criterion
        self.explanatory = explanatory
        self.target = target
        self.root.sub_population = np.ones_like(self.target, dtype="bool")
        if self._is_leaf_population(self.root.sub_population, self.root.depth):
            values, counts = np.unique(self.target, return_counts=True)
            self.root = Leaf(values[np.argmax(counts)], depth=0)
            self.root.is_root = True
            self.root.sub_population = np.ones_like(
                self.target,
                dtype="bool",
            )
        else:
            self.fit_node(self.root)
        self.update_predict()
        if verbose == 1:
            print(
                "  Training finished.\n"
                f"    - Depth                     : {self.depth()}\n"
                f"    - Number of nodes           : {self.count_nodes()}\n"
                "    - Number of leaves          : "
                f"{self.count_nodes(only_leaves=True)}\n"
                "    - Accuracy on training data : "
                f"{self.accuracy(self.explanatory, self.target)}"
            )

    def accuracy(self, test_explanatory, test_target):
        """Compute the accuracy on a dataset."""
        predictions = self.predict(test_explanatory)
        return np.sum(np.equal(predictions, test_target)) / test_target.size
