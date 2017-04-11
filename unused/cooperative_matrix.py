from unused.d_transforms import *

t = Symbol('t')
# t_value = 1.55
# k = 5
# S_matrix = [[1, -t], [t, 0]]


def e_image_2(mul1, level, t_value):
    expr_with_value = (t_value ** level) / factorial(level)
    return expr_with_value * mul1


def return_vander_array(k_value):
    x_vec = [0 for x in range(k_value)]
    for k in range(0, k_value):
        x_vec[k] = k+1
    return np.vander(x_vec, k_value, increasing=True)


def e_image_vec(mul1, k_value, t_value):
    x_item = [0 for x in range(k_value)]
    for k in range(0, k_value):
        x_item[k] = factorial(k) * e_image_2(mul1, k, t_value)
    return x_item


def exponential_c_2(mul1, image, k_value, t_value):
    c_vec = inverse_matrix(return_vander_array(k_value)).dot(e_image_vec(mul1, k_value, t_value))
    return c_vec


def recover_e_image_values(mul1, image, k_value, t_value):
    item = 0

    c_vec = exponential_c_2(mul1, image, k_value + 1, t_value)
    for k in range(0, k_value + 1):
        c_value = c_vec[k]
        item += exp(k * (t-t_value)) * c_value
        print("K = " + str(k))
        print("C_ (" + str(k) + ") = " + str(c_value))
        print("X (" + str(k) + ") = " + str(e_image_2(mul1, k, t_value)))

    return exp(-(t-t_value)) * item


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
                multiplied = recover_e_image_values(mul1, exp(t), k, t_value)

                e_matrix[i][j] = multiplied

    return e_matrix


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


def cooperative_matrix(matrix_a, matrix_b, k, t_value_):

    matrix = [[0] * len(matrix_a) for x in range(len(matrix_a))]
    t_value = t_value_

    matrix = exponential_matrix(matrix_a, matrix_b, k, t_value)
    print(matrix)

    return matrix


matrix_a = [[40, 10], [50, 15]]
matrix_b = [[40, 50], [10, 15]]


k = 3

t_value_ = 0.8

cooperative_matrix(matrix_a, matrix_b, k, t_value_)

