from sympy import *
import numpy as np

t = Symbol('t')
d = Symbol('d')


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


def item_transform(item, level, t_value):
    if level == 0:
        return item.evalf(subs={t: t_value})
    derivative = diff(item, t, level)
    expr_with_value = derivative.evalf(subs={t: t_value})
    return expr_with_value / factorial(level)


def differential_transform(_matrix, level):
    "returns a differential of given matrix"
    rows = len(_matrix)
    columns = len(_matrix[0])
    z_matrix = [[0] * columns for x in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            z_matrix[i][j] = item_transform(_matrix[i][j], level, 0)
    return z_matrix


def differential_vector(_vector, level, t_value):
    "returns a differential of given vector"
    _length = len(_vector)
    z_vector = np.empty([_length])
    for i in range(0, _length):
        z_vector[i] = item_transform(_vector[i], level, t_value)
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
        value += item_transform(value1, k_value - l, 0) * item_transform(value2, k_value, 0)
    return value


def divide_image_values(value1, value2, k_value):
    mul = multiply_image_values(value1, value2, k_value)
    return (item_transform(value1, k_value, 0) - mul) / item_transform(value2, 0, 0)


#####################################################################
#                   SIMPLEX TRANSFORMATIONS
#####################################################################

def is_number(s):
    try:
        float(s)
        return True
    except TypeError:
        return False


def set_matrix_parameter(matrix, level):
    rows = len(matrix)
    columns = len(matrix[0])
    result = [[0] * columns for x in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            if is_number(matrix[i][j]):
                result[i][j] = matrix[i][j]
            else:
                result[i][j] = matrix[i][j].evalf(subs={t: 0})
    return result


