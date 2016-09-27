from TransformationUtils import *

t = Symbol('t')

S_matrix = [[1, 1 - t], [t, 0]]

print(S_matrix)


def multiply_image_matrix(matrix, k):
    _length = len(matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for l in range(0, k + 1):
        z_matrix += np.dot(differential_transform(matrix, l), differential_transform(matrix, k - l))
    return z_matrix


def item_transformation(item, level):
    if level == 0:
        return item.evalf(subs={t: 1.2})
    derivative = diff(item, t, level)
    expr_with_value = derivative.evalf(subs={t: 1.2})
    return expr_with_value / factorial(level)


def multiply_images(value1, value2, k_value):
    value = 0
    for l in range(0, k_value + 1):
        value += item_transformation(value1, k_value - l) * item_transformation(value2, k_value)
    return value


def exponential_c_values(image1, image2, k_value):
    item = 0
    for k in range(0, k_value + 1):
        item += exponential_c_values(image1, image2, k)*multiply_images(image1, image2, k_value - k - 1)
    return (1/multiply_images(image1, image2, 0))*item


def recover_exponential_image_values(image1, image2, k_value):
    item = 0
    for k in range(0, k_value + 1):
        item += t ** k * exponential_c_values(image1, image2, k)
    return 1/item


item1 = t*exp(-0.8*(0.5040+t))
item2 = t
print(multiply_images(item1, item2, 2))
print(recover_exponential_image_values(item1, item2, 2))
