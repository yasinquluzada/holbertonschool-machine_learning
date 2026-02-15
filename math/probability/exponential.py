#!/usr/bin/env python3
"""Exponential distribution module.

Defines the Exponential class used to model an exponential distribution and
estimate its rate parameter (lambtha) from sample data.
"""


class Exponential:
    """Exponential distribution.

    lambtha is the expected number of occurrences in a given time frame.
    """

    def __init__(self, data=None, lambtha=1.):
        """Initialize an Exponential distribution.

        Args:
            data (list, optional): Sample data to estimate lambtha.
            lambtha (float, optional): Rate parameter when data is None.

        Raises:
            TypeError: If data is not a list.
            ValueError: If lambtha is not positive, or data has < 2 values.
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

        total = 0.0
        for x in data:
            total += x
        self.lambtha = float(len(data)) / total
