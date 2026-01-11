#!/usr/bin/env python3
"""Concat module."""


index = __import__('10-index').index
pd = __import__('pandas')


def concat(df1, df2):
    """Index on Timestamp, prepend filtered bitstamp rows, and add source keys.

    Args:
        df1: pandas.DataFrame (coinbase).
        df2: pandas.DataFrame (bitstamp).

    Returns:
        pandas.DataFrame: Concatenated DataFrame with keys.
    """
    df1_i = index(df1)
    df2_i = index(df2)
    df2_sel = df2_i[df2_i.index <= 1417411920]
    return pd.concat([df2_sel, df1_i], keys=["bitstamp", "coinbase"])
