#!/usr/bin/env python3
"""Prune module."""


def prune(df):
    """Remove rows where the Close column has NaN values.

    Args:
        df: pandas.DataFrame.

    Returns:
        pandas.DataFrame: DataFrame with NaN Close rows removed.
    """
    return df[df["Close"].notna()]
