#!/usr/bin/env python3
def matrix_transpose(matrix):
    return [list(col) for col in zip(*matrix)]