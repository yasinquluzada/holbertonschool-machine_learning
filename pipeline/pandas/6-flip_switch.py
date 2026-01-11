#!/usr/bin/env python3
"""Flip it and Switch it module."""


def flip_switch(df):
    """Sort the data in reverse chronological order and transpose it.

    Args:
        df: pandas.DataFrame.

    Returns:
        pandas.DataFrame: The transformed DataFrame.
    """
    return df.sort_index(ascending=False).T
