from project_files.services.transformation_util import *

t = Symbol('t')
# t_value = 1.55
# k = 5
# S_matrix = [[1, -t], [t, 0]]


def exponential_matrix(matrix_a, matrix_b, k, t_value):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    e_matrix = [[0] * columns for x in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            item1 = matrix_a[i][j]
            item2 = matrix_b[i][j]
            if is_number(item1):
                print("i = " + str(i) + "j = " + str(j))
                derive = item1 * exp(-(item1 - item2)*t)
                multiplied = recover_exponential_image_values(derive, k, t_value)
                # formatted = float("{0:.5f}".format(multiplied))
                e_matrix[i][j] = multiplied

    return e_matrix


# def multiply_image_matrix(matrix, k):
#     _length = len(matrix)
#     z_matrix = [[0] * _length for x in range(_length)]
#     for l in range(0, k + 1):
#         z_matrix += np.dot(differential_transform(matrix, l), differential_transform(matrix, k - l))
#     return z_matrix

def set_value_to_matrix(matrix, t_value):
    rows = len(matrix)
    columns = len(matrix[0])
    e_matrix = [[0] * columns for x in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            item = matrix[i][j]
            if is_number(item):
                e_matrix[i][j] = item
            else:
                e_matrix[i][j] = item.evalf(subs={t: t_value})
    print(e_matrix)
    return e_matrix


def get_matrix_b(matrix_a):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    b_matrix = [[0] * columns for x in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            item = matrix_a[i][j]
            if i == j:
                b_matrix[i][j] = item
            else:
                b_matrix[i][j] = -item
    return b_matrix


def cooperative_matrix(matrix_a, matrix_b, iterations, k, t_value_):

    with open("Output.txt", "w") as text_file:
        print('--------- COOPERATIVE GAME MODEL SOLUTION -------------', file=text_file)

    matrix = [[0] * len(matrix_a) for x in range(len(matrix_a))]
    t_value = t_value_
    for iteration in range(0, iterations):
        # matrix_a = matrix
        # matrix_b = get_matrix_b(matrix_a)
        matrix = exponential_matrix(matrix_a, matrix_b, k, t_value)
        print(matrix)

    return matrix


matrix_a = [[40, 10], [50, 15]]
matrix_b = [[40, 50], [10, 15]]

iterations = 1

k = 3

t_value_ = 0.8

cooperative_matrix(matrix_a, matrix_b, 1, k, t_value_)

