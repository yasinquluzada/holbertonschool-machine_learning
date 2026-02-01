#!/usr/bin/env python3

def add_arrays(arr1, arr2):
    rows = len(arr1)
    columns = len(arr2[0])
    for i in range(rows):
        for j in range(columns):
            arr1[i][j] = arr2[i][j] + arr1[i][j]
