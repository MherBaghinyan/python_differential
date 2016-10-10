from TransformationUtils import *

t = Symbol('t')

S_matrix = [[1, -t], [t, 0]]

print(S_matrix)


def exponential_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    e_matrix = [[0] * columns for x in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            item = matrix[i][j]
            if is_number(item):
                e_matrix[i][j] = item*exp(-0.8*(item-item))
            else:
                e_matrix[i][j] = recover_exponential_image_values(item, exp(-0.1*(item+item)), 1).evalf(subs={t: 1.55})
    return e_matrix


def multiply_image_matrix(matrix, k):
    _length = len(matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for l in range(0, k + 1):
        z_matrix += np.dot(differential_transform(matrix, l), differential_transform(matrix, k - l))
    return z_matrix


def item_transformation(item, level):
    return diff(item, t, level) / factorial(level)


def multiply_images(value1, value2, k_value):
    value = 0
    for l in range(0, k_value + 1):
        value += item_transformation(value1, k_value - l) * item_transformation(value2, k_value)
    return value


def exponential_c_values(image1, image2, k_value):
    item = 0
    if k_value == 0:
        return 1/multiply_images(image1, image2, 0)
    for k in range(0, k_value):
        item += exponential_c_values(image1, image2, k)*multiply_images(image1, image2, k_value - k)
    return (1/multiply_images(image1, image2, 0))*item


def recover_exponential_image_values(image1, image2, k_value):
    item = 0
    for k in range(0, k_value + 1):
        item += t ** k * exponential_c_values(image1, image2, k)
    return 1/item


item1 = t*exp(-0.1*(t+t))
item2 = t
print(multiply_images(item1, item2, 2))
result = recover_exponential_image_values(item1, item2, 2)
print(result)
print(result.evalf(subs={t: 1.55}))
print(exponential_matrix(S_matrix))


