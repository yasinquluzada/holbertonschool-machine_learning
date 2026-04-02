#!/usr/bin/env python3
"""Decision tree module with leaf collection support."""

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

    def max_depth_below(self):
        """Return the maximum depth under this node."""
        depths = [self.depth]
        if self.left_child is not None:
            depths.append(self.left_child.max_depth_below())
        if self.right_child is not None:
            depths.append(self.right_child.max_depth_below())
        return max(depths)

    def get_leaves_below(self):
        """Return the list of leaves under this node."""
        leaves = []
        if self.left_child is not None:
            leaves.extend(self.left_child.get_leaves_below())
        if self.right_child is not None:
            leaves.extend(self.right_child.get_leaves_below())
        return leaves


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

    def get_leaves_below(self):
        """Return this leaf in a list."""
        return [self]

    def __str__(self):
        """Return the string representation of the leaf."""
        return "-> leaf [value={}] ".format(self.value)


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

    def get_leaves(self):
        """Return all leaves of the tree."""
        return self.root.get_leaves_below()
