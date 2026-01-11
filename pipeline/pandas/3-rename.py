#!/usr/bin/env python3
"""Rename Timestamp to Datetime and keep only Datetime and Close columns."""


import pandas as pd


def rename(df):
    """Rename Timestamp to Datetime, convert to datetime, and select columns.

    Args:
        df (pandas.DataFrame): DataFrame containing a 'Timestamp' column.

    Returns:
        pandas.DataFrame: DataFrame with 'Datetime' and 'Close' columns only.
    """
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
