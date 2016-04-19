from sympy import *
import numpy as np

t = Symbol('t')

def get_max_k(matrix):
    level = 0
    while np.count_nonzero(differential_transform(matrix, level)) > 0:
        level += 1
    return level

def differential_transform(_matrix, level):
    "returns a differential of given matrix"
    _length = len(_matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for i in range(0, _length):
        for j in range(0, _length):
            express = diff(_matrix[i][j], t, level)
            exprWithValue = express.evalf(subs={t: 0})
            z_matrix[i][j] = int(exprWithValue / factorial(level))
    return z_matrix