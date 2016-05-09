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

def item_transform(item, level):
    derivative = diff(item, t, level)
    expr_with_value = derivative.evalf(subs={t: 0})
    return int(expr_with_value / factorial(level))

def differential_transform(_matrix, level):
    "returns a differential of given matrix"
    _length = len(_matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for i in range(0, _length):
        for j in range(0, _length):
            z_matrix[i][j] = item_transform(_matrix[i][j], level)
    return z_matrix

def differential_vector(_vector, level):
    "returns a differential of given vector"
    _length = len(_vector)
    z_vector = np.empty([_length])
    for i in range(0, _length):
        z_vector[i] = item_transform(_vector[i], level)
    return z_vector

def inverse_matrix(matrix):
    "returns inverse of a given matrix"
    return np.linalg.inv(matrix)

def transform_and_inverse(matrix, level):
    "transforms given matrix and returns it's inverse"
    return inverse_matrix(differential_transform(matrix, level))

def multiply_image_values(value1, value2, k_value):
    value = 0
    for l in range(0, k_value + 1):
        value += item_transform(value1, k_value - l) * item_transform(value2, k_value)
    return value

def divide_image_values(value1, value2, k_value):
    mul = multiply_image_values(value1, value2, k_value)
    return (item_transform(value1, k_value) - mul) / item_transform(value2, 0)
