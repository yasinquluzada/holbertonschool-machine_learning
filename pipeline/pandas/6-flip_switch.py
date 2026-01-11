#!/usr/bin/env python3
"""Flip it and Switch it module."""


import pandas as pd


def flip_switch(df):
    """Sort the data in reverse chronological order, then transpose it.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas.DataFrame")
    return df.sort_index(ascending=False).T
