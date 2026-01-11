#!/usr/bin/env python3
"""Indexing module."""


def index(df):
    """Set the Timestamp column as the index of the DataFrame.

    Args:
        df: pandas.DataFrame.

    Returns:
        pandas.DataFrame: DataFrame indexed by Timestamp.
    """
    return df.set_index("Timestamp")
