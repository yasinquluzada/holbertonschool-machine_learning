#!/usr/bin/env python3



def np_slice(matrix, axes={}):
    
    slices = [slice(None)] * matrix.ndim
    for axis, slc in axes.items():
        slices[axis] = slice(*slc)
    return matrix[tuple(slices)].copy()
