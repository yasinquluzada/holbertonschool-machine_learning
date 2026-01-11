#!/usr/bin/env python3
"""Hierarchy module."""


import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Create a Timestamp-first hierarchical index and concatenate two tables.

    Args:
        df1 (pd.DataFrame): Coinbase DataFrame.
        df2 (pd.DataFrame): Bitstamp DataFrame.

    Returns:
        pd.DataFrame: Concatenated DataFrame with (Timestamp, exchange) index.
    """
    df1 = index(df1)
    df2 = index(df2)

    start = 1417411980
    end = 1417417980

    df1 = df1.sort_index().loc[start:end]
    df2 = df2.sort_index().loc[start:end]

    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
    df = df.swaplevel(0, 1).sort_index()
    return df
