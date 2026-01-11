#!/usr/bin/env python3
"""Slice specific columns and rows from a pandas DataFrame."""


def slice(df):
    """Extract High, Low, Close, and Volume_(BTC) columns and every 60th row.

    Args:
        df: pandas.DataFrame to slice.

    Returns:
        pandas.DataFrame: Sliced DataFrame.
    """
    cols = ["High", "Low", "Close", "Volume_(BTC)"]
    return df.loc[::60, cols]
