from project_files.services.transformation_util import *

t = Symbol('t')

S_matrix = [[1 + t, 1 - t], [-t, t ** 2]]

# S_matrix = [[cos(t) + t,     t + 5,     4*t**2 - 3*t,   0,              1],
#             [t + 2,         1,          3*t + 5,        sin(t),         0],
#             [t**3,          1,          t**2 + 1,        cos(t + 1),    0],
#             [exp(t),        sin(2 * t), 0,              1,              t],
#             [1,             0,          0,              0,              t]]

print(S_matrix)


def multiply_image_matrix(matrix, k):
    _length = len(matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for l in range(0, k + 1):
        z_matrix += np.dot(differential_transform(matrix, l), differential_transform(matrix, k - l))
    return z_matrix


def multiply_p_values(n_value, i, k_value):
    value = 0
    for l in range(0, k_value + 1):
        value += get_s_number(n_value - i, l) * get_p_image(i, k_value - l)
    return value


def get_s_number(n_value, k_value):
    if n_value > 1:
        matrix = multiply_image_matrix(S_matrix, k_value)
    else:
         matrix = differential_transform(S_matrix, k_value)
    _length = len(matrix)
    sum = 0
    for n in range(0, _length):
        sum += matrix[n][n]
    return sum


def get_p_image(n_value, k_value):
    item = get_s_number(n_value, k_value)
    addition = 0
    for i in range(1, n_value - 1 + 1):
            addition += multiply_p_values(n_value, i, k_value)
    result = (1 / n_value) * (item - addition)
    print("n = ", n_value, "k = ", k_value, "p = ", result)
    return result


def p_items( n, k_value):
    item = 0
    for k in range(0, k_value + 1):
        item += (t ** k / factorial(k)) * get_p_image(n, k)
    return item


def calculate_leverrier(n_value, k_value):
    p_item = [0 for x in range(n_value)]
    for n in range(1, n_value + 1):
        p_item[n - 1] = p_items(n, k_value)
    return p_item

k_max = get_max_k(S_matrix)
print(calculate_leverrier(len(S_matrix), k_max))
