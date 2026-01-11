#!/usr/bin/env python3
"""Flip and switch a DataFrame: reverse-chronological sort then transpose."""


import pandas as pd


def flip_switch(df):
    """Sort the DataFrame in reverse chronological order and transpose it.

    Args:
        df: pandas.DataFrame.

    Returns:
        pandas.DataFrame: The sorted and transposed DataFrame.
    """
    return df.sort_index(ascending=False).T
