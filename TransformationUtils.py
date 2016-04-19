from sympy import *
import numpy as np

t = Symbol('t')

def get_max_k(matrix):
    level = 0
    while np.count_nonzero(differential(matrix, level)) > 0 and level < 10:
        level += 1
    return level

def differential(matrix, level):
    "returns a differential of given matrix"
    _length = len(matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for i in range(0, _length):
        for j in range(0, _length):
            z_matrix[i][j] = diff(matrix[i][j], t, level)
    return z_matrix


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

def differential_vector(_vector, level):
    "returns a differential of given vector"
    _length = len(_vector)
    z_vector = np.empty([_length])
    for i in range(0, _length):
        express = diff(_vector[i], t, level).evalf(subs={t: 0})
        z_vector[i] = int(express / factorial(level))
    return z_vector

def inverse_matrix(matrix):
    "returns inverse of a given matrix"
    return np.linalg.inv(matrix)

def transform_and_inverse(matrix, level):
    "transforms given matrix and returns it's inverse"
    return inverse_matrix(differential_transform(matrix, level))
