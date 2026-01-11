#!/usr/bin/env python3
"""Analyze module."""


def analyze(df):
    """Compute descriptive statistics excluding the Timestamp column.

    Args:
        df: pandas.DataFrame.

    Returns:
        pandas.DataFrame: Descriptive statistics for all non-Timestamp columns.
    """
    data = df.drop(columns=["Timestamp"], errors="ignore")
    return data.describe()
