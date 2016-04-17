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
            exprWithValue = express.evalf(subs={t: level})
            z_matrix[i][j] = int(exprWithValue)
    return z_matrix

def multiply_image_matrix(matrix, k):
    _length = len(matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for l in range(0, _length):
        z_matrix += np.dot(differential_transform(matrix, l), differential_transform(matrix, k - l))
        print(z_matrix)
    return z_matrix

def p_items(matrix, index):
    count = len(S_matrix)
    for k in range(0, index):
        (1 / k) * (differential_transform(S_matrix, k))

def get_s_number(matrix):
    _length = len(matrix)
    sum = 0
    for n in range(0, _length):
        sum += matrix[n][n]
    return sum



def calculateLeverrier(start, end):
    count = len(S_matrix)
    p_item = [0 for x in range(len(S_matrix))]
    for n in range(start, end):
        p_items(S_matrix, n)
        print(p_item[n])
    return p_item

print(multiply_image_matrix(S_matrix, 1))

# print(calculateLeverrier(1, len(S_matrix)))
