#!/usr/bin/env python3
"""Fill missing values in a Coinbase/Bitstamp OHLCV DataFrame."""


def fill(df):
    """Apply required filling rules to the DataFrame.

    Steps:
    - Remove Weighted_Price column.
    - Fill missing Close values with previous row's Close (forward fill).
    - Fill missing Open/High/Low with the Close value of the same row.
    - Fill missing Volume_(BTC) and Volume_(Currency) with 0.

    Args:
        df: pandas.DataFrame.

    Returns:
        pandas.DataFrame: Modified DataFrame.
    """
    if "Weighted_Price" in df.columns:
        df = df.drop(columns=["Weighted_Price"])

    if "Close" in df.columns:
        df["Close"] = df["Close"].ffill()

    for col in ("Open", "High", "Low"):
        if col in df.columns and "Close" in df.columns:
            df[col] = df[col].fillna(df["Close"])

    for col in ("Volume_(BTC)", "Volume_(Currency)"):
        if col in df.columns:
            df[col] = df[col].fillna(0)

    return df
