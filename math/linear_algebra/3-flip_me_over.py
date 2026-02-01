#!/usr/bin/env python3

def matrix_transpose(matrix):
    #return [list(col) for col in zip(*matrix)]

    rows = len(matrix)
    columns = (len(matrix[0]))
    return [[matrix[r][c] for r in range(rows)]] for c in range(cols)]
