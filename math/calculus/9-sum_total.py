#!/usr/bin/env python3
"""
Module 9-sum_total
Contains a function to compute the summation of i squared from 1 to n.
"""


def summation_i_squared(n):
    """
    Calculate the sum of i^2 from i=1 to i=n.

    Args:
        n (int): stopping condition

    Returns:
        int | None: integer sum if n is a valid positive integer, otherwise None
    """
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        return None
    return (n * (n + 1) * (2 * n + 1)) // 6
