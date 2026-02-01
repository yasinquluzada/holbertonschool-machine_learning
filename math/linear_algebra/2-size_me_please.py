#!/usr/bin/env python3

def matrix_shape(matrix):
    if type(matrix) is not list:
        return []

    if len(matrix) == 0:
        return [0]


    return [len(matrix)] + matrix_shape(matrix[0])