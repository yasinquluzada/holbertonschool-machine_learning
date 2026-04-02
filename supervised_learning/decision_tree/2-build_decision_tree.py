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

    def max_depth_below(self):
        """Return the maximum depth below this node."""
        return max(
            self.left_child.max_depth_below(),
            self.right_child.max_depth_below(),
        )

    def left_child_add_prefix(self, text):
        """Add prefix to the left child string."""
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"
        for line in lines[1:]:
            new_text += "    |  " + line + "\n"
        return new_text

    def right_child_add_prefix(self, text):
        """Add prefix to the right child string."""
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"
        for line in lines[1:]:
            new_text += "       " + line + "\n"
        return new_text

    def __str__(self):
        """Return the string representation of the node."""
        if self.is_root:
            text = (
                f"root [feature={self.feature}, "
                f"threshold={self.threshold}]\n"
            )
        else:
            text = (
                f"-> node [feature={self.feature}, "
                f"threshold={self.threshold}]\n"
            )
        text += self.left_child_add_prefix(str(self.left_child))
        text += self.right_child_add_prefix(str(self.right_child))
        return text


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

    def __str__(self):
        """Return the string representation of the leaf."""
        return f"-> leaf [value={self.value}]"


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

    def __str__(self):
        """Return the string representation of the tree."""
        return self.root.__str__()
