from project_files.services.transformation_util import *

t = Symbol('t')
A_matrix = [[t ** 2, -t + 1, 1], [t + 2, t, t ** 2], [0, 1, t]]
E_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
C_vector = [-2*(t ** 2), t*(t ** 3 + t ** 2 + 2), t*(t ** 2 + t - 1)]

print(A_matrix)


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
        if k > 0:
            result += differential_transform(matrix, p) * a_addition(matrix, k - p)
    return result


def x_image_transform(matrix, vector, index):
    return a_addition(matrix, index) * differential_vector(vector, index, 0)


def last_part(matrix, vector, k):
    _length = len(matrix)
    result = [[0] * _length for x in range(_length)]
    for p in range(1, k + 1):
        if k > 0:
            result += (differential_transform(matrix, p) * x_image_transform(matrix, vector, k - p))
    return result

def calculateTransform(k_max):
    x_item = [0 for x in range(len(C_vector))]
    a_inverse = transform_and_inverse(A_matrix, 0)
    for k in range(0, k_max):
        last_p = last_part(A_matrix, C_vector, k)
        step = a_inverse * (differential_vector(C_vector, k) - last_p)
        x_item[k] = step * (t ** k)
        print(x_item[k])
    return x_item


# k_max = get_max_k(A_matrix)
# print(calculateTransform(k_max))


# print(np.dot(A_matrix, A_matrix))
# np.linalg.inv(np.matrix(differential_transform(A_matrix, 0)))
