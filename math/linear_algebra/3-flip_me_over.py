#!/usr/bin/env python3

def matrix_transpose(matrix):

    for i, j in zip(*matrix):
        print(i, j)