#!/usr/bin/env python3
"""Polynomial derivative module."""


def poly_derivative(poly):
    """Calculate the derivative of a polynomial represented by a list."""
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    for coef in poly:
        if isinstance(coef, bool) or not isinstance(coef, (int, float)):
            return None

    if len(poly) == 1:
        return [0]

    derivative = [coef * power for power, coef in enumerate(poly[1:], start=1)]

    while len(derivative) > 1 and derivative[-1] == 0:
        derivative.pop()

    if all(value == 0 for value in derivative):
        return [0]

    return derivative
