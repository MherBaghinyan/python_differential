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
                mul1 = item1 * exp(-(item1 - item2))
                multiplied = recover_exponential_image_values(mul1, exp(t), k, t_value)
                # formatted = float("{0:.5f}".format(multiplied))
                e_matrix[i][j] = multiplied

    return e_matrix


# def multiply_image_matrix(matrix, k):
#     _length = len(matrix)
#     z_matrix = [[0] * _length for x in range(_length)]
#     for l in range(0, k + 1):
#         z_matrix += np.dot(differential_transform(matrix, l), differential_transform(matrix, k - l))
#     return z_matrix


def item_transformation(item, level, t_value):
    derivative = diff(item, t, level)
    expr_with_value = derivative.evalf(subs={t: t_value})
    return (t_value ** level) / factorial(level)


# def multiply_images(value, k_value, t_value):
#     return item_transformation(value, k_value, t_value) / factorial(k_value)


def exponential_c_values(mul1, image, k_value, t_value):
    item = 0
    if k_value == 0:
        return 1/(mul1 * item_transformation(image, 0, t_value))
    for k in range(0, k_value):
        item += exponential_c_values(mul1, image, k, t_value) * mul1 * item_transformation(image, k_value, t_value)
    return (1/(mul1 * item_transformation(image, 0, t_value)))*(1/factorial(k_value) - item)


def recover_exponential_image_values(mul1, image, k_value, t_value):
    item = 0
    for k in range(0, k_value + 1):
        exp_value = exponential_c_values(mul1, image, k, t_value)
        item += (t-t_value) ** k * exp_value
        print("exp (" + str(k) + ")" + str(exp_value))
        print("X (" + str(k) + ")" + str(mul1 * item_transformation(image, k, t_value)))
    return exp(t-t_value)/item


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
    matrix = [[0] * len(matrix_a) for x in range(len(matrix_a))]
    t_value = t_value_
    for iteration in range(0, iterations):
        # matrix_a = matrix
        # matrix_b = get_matrix_b(matrix_a)
        matrix = exponential_matrix(matrix_a, matrix_b, k, t_value)
        print(matrix)

    return matrix

