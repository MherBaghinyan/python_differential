from sympy import *
import numpy as np

t = Symbol('t')
S_matrix = [[1 + t, 1 - t], [-t, t ** 2]]

print(S_matrix)

def differential_transform(_matrix, level):
    "returns a differential of given matrix"
    _length = len(_matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for i in range(0, _length):
        for j in range(0, _length):
            express = diff(_matrix[i][j], t, level)
            exprWithValue = express.evalf(subs={t: 0})
            z_matrix[i][j] = int(exprWithValue)
    return z_matrix

def multiply_image_matrix(matrix, k):
    _length = len(matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for l in range(0, _length):
        z_matrix += np.dot(differential_transform(matrix, l), differential_transform(matrix, k - l))
        print(z_matrix)
    return z_matrix

def get_s_number(n_value, k_value):
    if n_value > 1 :
        matrix = multiply_image_matrix(S_matrix, k_value)
    else:
         matrix = differential_transform(S_matrix, k_value)
    _length = len(matrix)
    sum = 0
    for n in range(0, _length):
        sum += matrix[n][n]
    return sum

def get_p_image(n_value, k_value):
    item = 1 / n_value * get_s_number(n_value, k_value)
    for l in range(1, k_value):
            for i in range(1, n_value - 1):
                item = - (1 / n_value) * get_s_number(n_value - i, l) * get_p_image(i, k_value - l)
    return item

def p_items(matrix, n, k_value):
    count = len(S_matrix)
    item = 0
    for k in range(1, k_value):
        item += (t ** k / factorial(k)) * get_p_image(n, k)
    return item

def calculate_Leverrier(n_value, k_value):
    count = len(S_matrix)
    p_item = [0 for x in range(count)]
    for n in range(1, n_value):
        p_item[n] = p_items(S_matrix, n, k_value)
        print(p_item[n])
    return p_item

print(calculate_Leverrier(2, 3))

