#!/usr/bin/env python3
"""Create a pandas DataFrame from a NumPy ndarray."""


import pandas as pd


def from_numpy(array):
    """Create a DataFrame from a NumPy ndarray with A..Z column labels.

    Args:
        array: NumPy ndarray.

    Returns:
        pandas.DataFrame: DataFrame with columns labeled A, B, C... in order.
    """
    ndim = getattr(array, "ndim", 0)
    n_cols = 1 if ndim < 2 else array.shape[1]
    columns = [chr(65 + i) for i in range(n_cols)]
    return pd.DataFrame(array, columns=columns)
