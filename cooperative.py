from transformation_util import *

t = Symbol('t')
t_value = 1.55
k = 5
S_matrix = [[1, -t], [t, 0]]
print(S_matrix)


def exponential_matrix(matrix_a, matrix_b, k, t_value, sympathy):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    e_matrix = [[0] * columns for x in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            item1 = matrix_a[i][j]
            item2 = matrix_b[i][j]
            if is_number(item1):
                multiplied = float(item1*exp(-sympathy*(item1 - item2)))
                # formatted = float("{0:.5f}".format(multiplied))
                e_matrix[i][j] = multiplied
            else:
                e_matrix[i][j] = recover_exponential_image_values(item1, exp(-sympathy*(item1 - item2)), k, t_value)
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
    return expr_with_value / factorial(level)


def multiply_images(value1, value2, k_value, t_value):
    value = 0
    for l in range(0, k_value + 1):
        value += item_transformation(value1, k_value - l, t_value) * item_transformation(value2, k_value, t_value)
    return value


def exponential_c_values(image1, image2, k_value, t_value):
    item = 0
    if k_value == 0:
        return 1/multiply_images(image1, image2, 0, t_value)
    for k in range(0, k_value):
        item += exponential_c_values(image1, image2, k, t_value)*multiply_images(image1, image2, k_value - k, t_value)
    return (1/multiply_images(image1, image2, 0, t_value))*(1/factorial(k_value) - item)


def recover_exponential_image_values(image1, image2, k_value, t_value):
    item = 0
    for k in range(0, k_value + 1):
        item += (t-t_value) ** k * exponential_c_values(image1, image2, k, t_value)
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
            if is_number(item) and  not (i == 0 and j == 1):
                b_matrix[i][j] = item
            else:
                b_matrix[i][j] = -item
    return b_matrix


def cooperative_matrix(matrix, iterations, k, t_value_, sympathy):
    t_value = t_value_
    for iteration in range(0, iterations):
        matrix_a = matrix
        matrix_b = get_matrix_b(matrix_a)
        matrix = exponential_matrix(matrix_a, matrix_b, k, t_value, sympathy)
        print(matrix)

    return matrix


# item1 = t
# # print(multiply_images(item1, exp(-0.1*(item1-item2)), 2))
# result = recover_exponential_image_values(item1, exp(-0.8*(item1-(-item1))), k)
# # recover_exponential_image_values(item1, exp(-sympathy*(item1 + item2)), k)
# print(result)
# #
# print(result.evalf(subs={t: t_value}))

iterated_matrix = S_matrix
# cooperative_matrix(iterated_matrix)

# for iteration in range(0, 3):
#     print(item_transformation(exp(-0.8*(item1-item2)), iteration))

