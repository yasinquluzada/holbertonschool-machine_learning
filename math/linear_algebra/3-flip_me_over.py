#!/usr/bin/env python3

def matrix_transpose(matrix):
    #return [list(col) for col in zip(*matrix)]




    for i in range(len(matrix)):
        for j in range(len(matrix(i))):
           matrix[i][j] = matrix[j][i]
