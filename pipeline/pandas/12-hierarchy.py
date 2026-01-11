#!/usr/bin/env python3
"""Hierarchy module."""


pd = __import__('pandas')
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Build a hierarchical index by timestamp and exchange.

    Rearranges the MultiIndex so that Timestamp is the first level, concatenates
    data from timestamps 1417411980 to 1417417980 (inclusive), adds keys
    (bitstamp for df2, coinbase for df1), and sorts chronologically.

    Args:
        df1: pandas.DataFrame (coinbase).
        df2: pandas.DataFrame (bitstamp).

    Returns:
        pandas.DataFrame: The concatenated DataFrame with hierarchical index.
    """
    df1 = index(df1)
    df2 = index(df2)

    start = 1417411980
    end = 1417417980

    if getattr(df1.index, "nlevels", 1) > 1:
        names1 = list(getattr(df1.index, "names", []))
        level1 = "Timestamp" if "Timestamp" in names1 else 0
        ts1 = df1.index.get_level_values(level1)
    else:
        ts1 = df1.index

    if getattr(df2.index, "nlevels", 1) > 1:
        names2 = list(getattr(df2.index, "names", []))
        level2 = "Timestamp" if "Timestamp" in names2 else 0
        ts2 = df2.index.get_level_values(level2)
    else:
        ts2 = df2.index

    df1 = df1[(ts1 >= start) & (ts1 <= end)]
    df2 = df2[(ts2 >= start) & (ts2 <= end)]

    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
    df = df.swaplevel(0, 1).sort_index()
    return df
