from sympy import *
import numpy as np

t = Symbol('t')
A_matrix = [[t ** 2, -t + 1, 1], [t + 2, t, t ** 2], [0, 1, t]]
E_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
C_vector = [-2*(t ** 2), t*(t ** 3 + t ** 2 + 2), t*(t ** 2 + t - 1)]

print(A_matrix)

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


def differential_vector(_vector, level):
    "returns a differential of given vector"
    _length = len(_vector)
    z_vector = np.empty([_length])
    for i in range(0, _length):
        express = diff(_vector[i], t, level).evalf(subs={t: level})
        z_vector[i] = int(express)
    return z_vector

def inverse_matrix(matrix):
    "returns inverse of a given matrix"
    return np.linalg.inv(matrix)

def transform_and_inverse(matrix, level):
    "transforms given matrix and returns it's inverse"
    return inverse_matrix(differential_transform(matrix, level))

def a_image_transform(matrix, k):
    "returns X image vector"
    _length = len(matrix)
    matrix_image = [[0] * _length for x in range(_length)]
    for i in range(0, _length):
        for j in range(0, i):
            matrix_image[i][j] = transform_and_inverse(matrix, 0) * a_addition(matrix, k)
    return matrix_image

def a_addition(matrix, k):
    _length = len(matrix)
    result = [[0] * _length for x in range(_length)]
    for p in range(1, k):
        if k > 1:
            result += differential_transform(matrix, p) * a_addition(matrix, k - p)
    return result

def x_image_transform(matrix, vector, index):
    return a_addition(matrix, index) * differential_vector(vector, index)

def last_part(matrix, vector, k):
    _length = len(matrix)
    result = [[0] * _length for x in range(_length)]
    for p in range(1, k):
        if k > 1:
            result += (differential_transform(matrix, p) * x_image_transform(matrix, vector, k - p))
    return result

def calculateTransform(start, end):
    x_item = [0 for x in range(len(C_vector))]
    for k in range(start, end):
        a_inverse = transform_and_inverse(A_matrix, 0)
        print(a_inverse)
        last_p = last_part(A_matrix, C_vector, k)
        step = a_inverse * (differential_vector(C_vector, k) - last_p)
        x_item[k] = np.multiply(step, (t ** k))
    return x_item

print(calculateTransform(0, 3))

# print(np.dot(A_matrix, A_matrix))
# np.linalg.inv(np.matrix(differential_transform(A_matrix, 0)))
