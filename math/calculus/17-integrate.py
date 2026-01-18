#!/usr/bin/env python3
"""Polynomial integration module."""


def poly_integral(poly, C=0):
    """Calculate the integral of a polynomial.

    Args:
        poly (list): List of coefficients where index is power of x.
        C (int): Integration constant.

    Returns:
        list: Integral coefficients list, or None if inputs are invalid.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, int):
        return None
    for coef in poly:
        if not isinstance(coef, (int, float)):
            return None

    integral = [C]
    for power, coef in enumerate(poly):
        value = coef / (power + 1)
        if isinstance(value, float) and value.is_integer():
            value = int(value)
        integral.append(value)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
