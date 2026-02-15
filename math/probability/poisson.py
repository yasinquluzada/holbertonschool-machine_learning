#!/usr/bin/env python3
"""Poisson distribution module."""


class Poisson:
    """Represents a Poisson distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize a Poisson distribution.

        Args:
            data (list): Data to estimate the distribution parameter.
            lambtha (float): Expected number of occurrences.

        Raises:
            TypeError: If data is not a list.
            ValueError: If lambtha is not a positive value.
            ValueError: If data does not contain multiple values.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))
