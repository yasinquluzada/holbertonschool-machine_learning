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
        left_depth = self.depth
        right_depth = self.depth
        if self.left_child is not None:
            left_depth = self.left_child.max_depth_below()
        if self.right_child is not None:
            right_depth = self.right_child.max_depth_below()
        return max(left_depth, right_depth)

    def left_child_add_prefix(self, text):
        """Add the left-child prefix to a subtree string."""
        lines = text.split("\n")
        new_lines = ["    +--" + lines[0]]
        for line in lines[1:]:
            new_lines.append("    |  " + line)
        return "\n".join(new_lines)

    def right_child_add_prefix(self, text):
        """Add the right-child prefix to a subtree string."""
        lines = text.split("\n")
        new_lines = ["    +--" + lines[0]]
        for line in lines[1:]:
            new_lines.append("       " + line)
        return "\n".join(new_lines)

    def __str__(self):
        """Return the string representation of the node."""
        node_type = "root" if self.is_root else "-> node"
        text = (
            f"{node_type} [feature={self.feature}, "
            f"threshold={self.threshold}]"
        )
        if self.left_child is not None:
            text += "\n" + self.left_child_add_prefix(str(self.left_child))
        if self.right_child is not None:
            text += "\n" + self.right_child_add_prefix(str(self.right_child))
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
