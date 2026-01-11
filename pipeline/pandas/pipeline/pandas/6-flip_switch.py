#!/usr/bin/env python3
"""Flip and switch a DataFrame: reverse-chronological sort then transpose."""


import pandas as pd


def flip_switch(df):
    """Sort df in reverse chronological order by index, then transpose.

    Args:
        df: pandas.DataFrame.

    Returns:
        pandas.DataFrame: Sorted then transposed DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas.DataFrame")
    return df.sort_index(ascending=False).T
