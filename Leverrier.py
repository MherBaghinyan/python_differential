from sympy import *
import numpy as np

t = Symbol('t')
S_matrix = [[1 + t, 1 - t], [-t, t ** 2]]

print(S_matrix)

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

def multiply_image_matrix(matrix, k):
    _length = len(matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for l in range(0, k + 1):
        z_matrix += np.dot(differential_transform(matrix, l), differential_transform(matrix, k - l))
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
    addition = 0
    for l in range(1, k_value + 1):
            for i in range(1, n_value - l + 1):
                addition +=  get_s_number(n_value - i, l) * get_p_image(i, k_value - l)
    result = (1 / n_value) * (item - addition)
    print("n = ", n_value, "k = ", k_value, "p = ", result)
    return result

def p_items( n, k_value):
    item = 0
    for k in range(1, k_value + 1):
        item += (t ** k / factorial(k)) * get_p_image(n, k)
    return item

def calculate_Leverrier(n_value, k_value):
    count = len(S_matrix)
    p_item = [0 for x in range(count)]
    for n in range(1, n_value + 1):
        p_item[n - 1] = p_items(n, k_value)
    return p_item

k_max = get_max_k(S_matrix)
print(calculate_Leverrier(2, k_max))
