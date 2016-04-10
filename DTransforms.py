from sympy import *
import numpy as np

t = Symbol('t')
A_matrix = [[t ** 2, -t + 1, 1], [t + 2, t, t ** 2], [0, 1, t]]
E_matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
E1_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
C_vector = [-2*(t ** 2), t*(t ** 3 + t ** 2 + 2), t*(t ** 2 + t - 1)]

print(A_matrix)

def differential_transform(_matrix, level):
    "returns a differential of given matrix"
    _length = len(_matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for i in range(0, _length):
        for j in range(0, _length):
            z_matrix[i][j] = int(diff(_matrix[i][j], t, level).evalf(subs={t: level}))
            print(z_matrix[i][j])
    return z_matrix


def differential_vector(_vector, level):
    "returns a differential of given vector"
    _length = len(_vector)
    z_vector = np.empty([_length])
    for i in range(0, _length):
            z_vector[i] = int(diff(_vector[i], t, level).evalf(subs={t: level}))
            print(z_vector[i])
    return z_vector

def calculateTransform(start, end):
    for k in range(start, end):
        a0 = differential_transform(A_matrix, 1)
        a_inverse = np.linalg.inv(a0)
        print(a_inverse)
        (t ** k) * a_inverse * (differential_vector(C_vector, k) * differential_transform(A_matrix, k))

calculateTransform(0, 3)

# print(np.dot(A_matrix, A_matrix))
# np.linalg.inv(np.matrix(differential_transform(A_matrix, 0)))
