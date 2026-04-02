#!/usr/bin/env python3
"""Decision tree module."""

import numpy as np


class Node:
    """Decision tree node."""

    def __init__(
        self,
        feature=None,
        threshold=None,
        left_child=None,
        right_child=None,
        is_root=False,
        depth=0,
    ):
        """Initialize a node."""
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth
        self.lower = {}
        self.upper = {}
        self.indicator = None

    def max_depth_below(self):
        """Return the maximum depth below this node."""
        depths = [self.depth]
        if self.left_child is not None:
            depths.append(self.left_child.max_depth_below())
        if self.right_child is not None:
            depths.append(self.right_child.max_depth_below())
        return max(depths)

    def count_nodes_below(self):
        """Return the number of nodes below this node."""
        left_count = 0
        right_count = 0
        if self.left_child is not None:
            left_count = self.left_child.count_nodes_below()
        if self.right_child is not None:
            right_count = self.right_child.count_nodes_below()
        return 1 + left_count + right_count

    def get_leaves_below(self):
        """Return the list of leaves below this node."""
        leaves = []
        if self.left_child is not None:
            leaves.extend(self.left_child.get_leaves_below())
        if self.right_child is not None:
            leaves.extend(self.right_child.get_leaves_below())
        return leaves

    def update_bounds_below(self):
        """Update the lower and upper bounds below this node."""
        if self.left_child is not None:
            self.left_child.lower = dict(self.lower)
            self.left_child.upper = dict(self.upper)
            self.left_child.lower[self.feature] = self.threshold
            self.left_child.update_bounds_below()
        if self.right_child is not None:
            self.right_child.lower = dict(self.lower)
            self.right_child.upper = dict(self.upper)
            self.right_child.upper[self.feature] = self.threshold
            self.right_child.update_bounds_below()

    def update_indicator(self):
        """Update the indicator function of the node."""

        def is_large_enough(x):
            """Return True for rows larger than all lower bounds."""
            if len(self.lower) == 0:
                return np.ones(x.shape[0], dtype=bool)
            return np.all(
                np.array(
                    [
                        np.greater(x[:, key], self.lower[key])
                        for key in self.lower
                    ]
                ),
                axis=0,
            )

        def is_small_enough(x):
            """Return True for rows smaller than all upper bounds."""
            if len(self.upper) == 0:
                return np.ones(x.shape[0], dtype=bool)
            return np.all(
                np.array(
                    [
                        np.less_equal(x[:, key], self.upper[key])
                        for key in self.upper
                    ]
                ),
                axis=0,
            )

        self.indicator = lambda x: np.all(
            np.array([is_large_enough(x), is_small_enough(x)]),
            axis=0,
        )

    def pred(self, x):
        """Return the prediction for one sample."""
        if x[self.feature] > self.threshold:
            return self.left_child.pred(x)
        return self.right_child.pred(x)
    



class Leaf(Node):
    """Decision tree leaf."""

    def __init__(self, value, depth=None):
        """Initialize a leaf."""
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """Return the depth of the leaf."""
        return self.depth

    def count_nodes_below(self):
        """Return the number of nodes below the leaf."""
        return 1

    def get_leaves_below(self):
        """Return the leaf in a list."""
        return [self]

    def update_bounds_below(self):
        """Keep the bounds unchanged for a leaf."""
        return None

    def pred(self, x):
        """Return the prediction for one sample."""
        return self.value
    



class Decision_Tree:
    """Decision tree."""

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
        if root is not None:
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

    def count_nodes(self):
        """Return the number of nodes in the tree."""
        return self.root.count_nodes_below()

    def get_leaves(self):
        """Return the list of leaves of the tree."""
        return self.root.get_leaves_below()

    def update_bounds(self):
        """Update bounds for all nodes of the tree."""
        self.root.lower = {}
        self.root.upper = {}
        self.root.update_bounds_below()

    def pred(self, x):
        """Return the prediction for one sample."""
        return self.root.pred(x)

    def update_predict(self):
        """Update the vectorized prediction function."""
        self.update_bounds()
        leaves = self.get_leaves()
        for leaf in leaves:
            leaf.update_indicator()
        self.predict = lambda A: np.sum(
            [leaf.indicator(A) * leaf.value for leaf in leaves],
            axis=0,
        )
    

    

