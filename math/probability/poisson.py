#!/usr/bin/env python3
"""Poisson distribution module."""


class Poisson:
    """Represents a Poisson distribution."""

    e = 2.718281828459045

    def __init__(self, data=None, lambtha=1.0):
        """Initialize a Poisson distribution.

        Args:
            data (list): List of observations to estimate lambtha.
            lambtha (float): Expected number of occurrences in a time frame.

        Raises:
            TypeError: If data is not a list.
            ValueError: If data has fewer than two values.
            ValueError: If lambtha is not a positive value.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
            return
        if type(data) is not list:
            raise TypeError("data must be a list")
        if len(data) < 2:
            raise ValueError("data must contain multiple values")
        self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculate the PMF for a given number of successes.

        Args:
            k (int): Number of successes.

        Returns:
            float: The PMF value for k.
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        term = self.e ** (-self.lambtha)
        i = 1
        while i <= k:
            term *= self.lambtha / i
            i += 1
        return term

    def cdf(self, k):
        """Calculate the CDF for a given number of successes.

        Args:
            k (int): Number of successes.

        Returns:
            float: The CDF value for k.
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        term = self.e ** (-self.lambtha)
        cdf_val = term
        i = 1
        while i <= k:
            term *= self.lambtha / i
            cdf_val += term
            i += 1
        return cdf_val
