#!/usr/bin/env python3

def matrix_transpose(matrix):
    if len(matrix) == 0:
        return []

    for i, j in zip(*matrix):
        print(i, j)