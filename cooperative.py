from TransformationUtils import *

t = Symbol('t')

S_matrix = [[1 + t, 1 - t], [-t, t ** 2]]

print(S_matrix)


def multiply_image_matrix(matrix, k):
    _length = len(matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for l in range(0, k + 1):
        z_matrix += np.dot(differential_transform(matrix, l), differential_transform(matrix, k - l))
    return z_matrix


