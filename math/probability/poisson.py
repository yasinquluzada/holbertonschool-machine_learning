#!/usr/bin/env python3
"""poisson
Defines a Poisson distribution class with PMF computation.
"""


class Poisson:
    """Poisson distribution.

    Represents a Poisson distribution parameterized by lambtha.
    """

    def __init__(self, data=None, lambtha=1.0):
        """Initialize a Poisson distribution.

        Args:
            data: List of data points to estimate lambtha from.
            lambtha: The expected number of occurrences (rate parameter).

        Raises:
            TypeError: If data is not a list.
            ValueError: If data has fewer than two values or lambtha <= 0.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
            return

        if not isinstance(data, list):
            raise TypeError("data must be a list")
        if len(data) < 2:
            raise ValueError("data must contain multiple values")

        self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculate the PMF for k occurrences.

        Args:
            k: Number of occurrences.

        Returns:
            The PMF value for k.
        """
        if k is None:
            return 0

        k = int(k)
        if k < 0:
            return 0

        lambtha = self.lambtha
        p = 1.0
        i = 1
        while i <= k:
            p *= lambtha / i
            i += 1

        e_neg = 1.0
        term = 1.0
        n = 1
        while n <= 120:
            term *= -lambtha / n
            e_neg += term
            n += 1

        return p * e_neg
