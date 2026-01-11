#!/usr/bin/env python3
"""Select last 10 rows of High and Close columns and return as a NumPy array."""


def array(df):
    """Return the last 10 rows of the High and Close columns as a NumPy array.

    Args:
        df: DataFrame containing 'High' and 'Close' columns.

    Returns:
        numpy.ndarray: Array of shape (10, 2) with columns [High, Close].
    """
    return df.loc[:, ["High", "Close"]].tail(10).to_numpy()
