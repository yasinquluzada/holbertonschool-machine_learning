#!/usr/bin/env python3
"""Load a delimited file into a pandas DataFrame."""


import pandas as pd


def from_file(filename, delimiter):
    """Load data from a file as a pandas DataFrame.

    Args:
        filename: Path to the file to load.
        delimiter: Column separator.

    Returns:
        pandas.DataFrame: Loaded data.
    """
    return pd.read_csv(filename, sep=delimiter)
