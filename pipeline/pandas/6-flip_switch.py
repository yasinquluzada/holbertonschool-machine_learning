#!/usr/bin/env python3
"""Flip and switch a DataFrame: reverse-chronological sort then transpose."""


import pandas as pd


def flip_switch(df):
    """Sort the data in reverse chronological order, then transpose it.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: The sorted and transposed DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas.DataFrame")
    return df.sort_index(ascending=False).T
