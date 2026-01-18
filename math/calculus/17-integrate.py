#!/usr/bin/env python3
"""Module that provides polynomial integration."""


def poly_integral(poly, C=0):
    """Return the integral of a polynomial represented by a list of coefficients."""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, int) or isinstance(C, bool):
        return None

    integral = [C]

    for power, coeff in enumerate(poly):
        if isinstance(coeff, bool) or not isinstance(coeff, (int, float)):
            return None
        if coeff != coeff or coeff in (float('inf'), float('-inf')):
            return None

        value = coeff / (power + 1)

        if isinstance(value, float) and value.is_integer():
            value = int(value)

        integral.append(value)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
