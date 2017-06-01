from sympy import *
import numpy as np
from copy import copy, deepcopy

d = Symbol('d')
t = Symbol('t')


def printTableu(tableu):
    print('----------------------')
    for row in tableu:
        print(row)
    print('----------------------')
    return


def write_table_file(table):
    with open("Output.txt", "a") as text_file:
        print('----------------------', file=text_file)
    for row in table:
        with open("Output.txt", "a") as text_file:
            print(row, file=text_file)

    return


# finds largest value
def find_largest_value(data):
    maximum = 0
    m, location = 0, 0
    maximum = data[0]

    for m in range(1, len(data)):
        if data[m] > maximum:
            maximum = data[m]
            location = m

    return location


# finds entering column
# column ==> in
def find_entering_column(data):
    max_negative = min([n for n in data if n < 0])

    if max_negative >= 0:
        return - 1

    for m in range(1, len(data)):
        if data[m] == max_negative:
            return m


# finds departing row
#  returns number
def find_departing_row(table, pivot_column):
    rows = len(table)
    values = [0 for x in range(rows - 1)]

    for i in range(1, rows):
        if table[i][pivot_column] > 0:
            values[i - 1] = table[i][0] / table[i][pivot_column]
        else:
            values[i - 1] = -1

    min_value = min([n for n in values if n >= 0])
    pivot_row = 0
    for i in range(0, rows):
        if values[i] == min_value:
            return i + 1


# generate next table
def form_next_table(table, pivot_row, pivot_column):
    columns = len(table[0])
    rows = len(table)

    pivot_value = table[pivot_row][pivot_column]

    pivot_vector = [0 for x in range(columns)]
    for j in range(0, columns):
        pivot_vector[j] = table[pivot_row][j] / pivot_value
        table[pivot_row][j] = pivot_vector[j]

    for i in range(0, rows):
        ratio = table[i][pivot_column]
        if i == pivot_row:
            continue
        for j in range(0, columns):
            multiplier = pivot_vector[j] * ratio
            table[i][j] -= multiplier

    return table


# main simplex method
def simplex_main(table):
    columns = len(table[0])
    rows = len(table) - 1

    array = table[0]
    pivot_column = find_entering_column(array)
    pivot_row = find_departing_row(table, pivot_column)

    print("pivot column", pivot_column)
    print("pivot row", pivot_row)

    while pivot_column >= 0:
        table = form_next_table(table, pivot_row, pivot_column)
        printTableu(table)

        if not any([n for n in array if n < 0]):
            break

        array = table[0]
        pivot_column = find_entering_column(array)
        pivot_row = find_departing_row(table, pivot_column)

    return table


def is_number(s):
    try:
        float(s)
        return True
    except TypeError:
        return False


def item_multi_transform(item, t_level, d_level, t_value, d_value):
    if t_level == 0 and d_level == 0:
        if is_number(item):
            return item
        return item.evalf(subs={t: t_value, d: d_value})
    if t_level == 0:
        d_derive = diff(item, d, d_level)
        return d_derive.evalf(subs={t: t_value, d: d_value}) / factorial(d_level)
    if d_level == 0:
        d_derive = diff(item, t, t_level)
        return d_derive.evalf(subs={t: t_value, d: d_value}) / factorial(t_level)
    derivative = diff(item, t, t_level)
    d_derive = diff(derivative, d, d_level)
    expr_with_value = d_derive.evalf(subs={t: t_value, d: d_value})
    return expr_with_value / (factorial(d_level) * factorial(t_level))


def matrix_multi_differential(matrix, t_level, d_level, t_value, d_value):
    "returns a differential of given matrix"
    _length = len(matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for i in range(0, _length):
        for j in range(0, _length):
            z_matrix[i][j] = item_multi_transform(matrix[i][j], t_level, d_level, t_value, d_value)
    return z_matrix


def prepare_matrix_for_simplex(s_matrix, k1, k2, t_value, d_value):
    simplex_matrix = []
    _length = len(s_matrix)
    z = []
    z.append(0.0)
    if_zero_step = k1 == 0 and k2 == 0
    for z_i in range(0, _length):
        if if_zero_step:
            z.append(-1.0)
        else:
            z.append(0.0)
    for z_i in range(0, _length):
        z.append(0.0)
    simplex_matrix.append(z)
    base_matrix = matrix_multi_differential(s_matrix, k1, k2, t_value, d_value)
    print("k1 ======= ", k1, "k2 ======= ", k2)
    printTableu(base_matrix)
    for m_i in range(0, _length):
        m_array = [0 for var in range(_length * 2 + 1)]
        for m_j in range(0, _length):
            if if_zero_step:
                m_array[0] = 1.0
            else:
                m_array[0] = 0.0
            m_array[m_j + 1] = base_matrix[m_i][m_j]
            if m_i == m_j and if_zero_step:
                m_array[_length + m_j + 1] = 1.0
            else:
                m_array[_length + m_j + 1] = 0.0
        simplex_matrix.append(m_array)
    return simplex_matrix


def get_image_matrixes(s_matrix, k1_value, k2_value, d_value, t_value):
    simplex_matrix = prepare_matrix_for_simplex(s_matrix, 0, 0, t_value, d_value)

    image_matrixes = [simplex_matrix * (k1_value + 1) for x in range(k2_value + 1)]
    for i in range(0, k1_value + 1):
        for j in range(0, k2_value + 1):
            image_matrixes[i][j] = prepare_matrix_for_simplex(s_matrix, i, j, t_value, d_value)
    return image_matrixes


def simplex_multi(table, image_matrixes, k1_value, k2_value):
    array = table[0]
    pivot_column = find_entering_column(array)
    pivot_row = find_departing_row(table, pivot_column)

    print("pivot column", pivot_column)
    print("pivot row", pivot_row)

    write_table_file(table)

    while pivot_column >= 0:
        image_matrixes = next_image_table(image_matrixes, pivot_row, pivot_column, k1_value, k2_value)

        table = image_matrixes[0][0]
        array = table[0]

        if not any([n for n in array if n < 0]):
            break

        pivot_column = find_entering_column(array)
        pivot_row = find_departing_row(table, pivot_column)

    return image_matrixes


# get division image value
def get_div_image(k1_value, k2_value, j, pivot_row, pivot_column, image_matrixes):
    item = 0

    a_i_0_j_0 = image_matrixes[0][0][pivot_row][pivot_column]

    if k1_value == 0 and k2_value == 0:
        return image_matrixes[0][0][pivot_row][j] / a_i_0_j_0

    if k1_value == 0 and k2_value != 0:
        for p2 in range(1, k2_value + 1):
            pivot_value = image_matrixes[0][p2][pivot_row][pivot_column]
            item += get_div_image(0, k2_value - p2, j, pivot_row, pivot_column, image_matrixes) * pivot_value
        return (image_matrixes[0][k2_value][pivot_row][j] - item) / a_i_0_j_0

    if k1_value != 0 and k2_value == 0:
        for p1 in range(1, k1_value + 1):
            pivot_value = image_matrixes[p1][0][pivot_row][pivot_column]
            item += get_div_image(k1_value - p1, 0, j, pivot_row, pivot_column, image_matrixes) * pivot_value
        return (image_matrixes[k1_value][0][pivot_row][j] - item) / a_i_0_j_0

    for p1 in range(1, k1_value + 1):
        for p2 in range(1, k2_value + 1):
            pivot_value = image_matrixes[p1][p2][pivot_row][pivot_column]
            item += get_div_image(k1_value - p1, k2_value - p2, j, pivot_row, pivot_column,
                                  image_matrixes) * pivot_value

    return (image_matrixes[k1_value][k2_value][pivot_row][j] - item) / a_i_0_j_0


def d_item_image(k1_value, k2_value, column, row, pivot_row, pivot_column, image_matrixes):
    d_item = 0

    for p1 in range(0, k1_value + 1):
        for p2 in range(0, k2_value + 1):
            row_0 = image_matrixes[k1_value - p1][k2_value - p2][pivot_row][column]
            col_0 = image_matrixes[p1][p2][row][pivot_column]
            d_item += row_0 * col_0

    return d_item


def b_item_image(k1_value, k2_value, column, row, pivot_row, pivot_column, image_matrixes):
    item = 0

    a_i_0_j_0 = image_matrixes[0][0][pivot_row][pivot_column]

    if k1_value == 0 and k2_value == 0:
        return d_item_image(0, 0, column, row, pivot_row, pivot_column, image_matrixes) / a_i_0_j_0

    if k1_value == 0 and k2_value != 0:
        for p2 in range(1, k2_value + 1):
            pivot_value = image_matrixes[0][p2][pivot_row][pivot_column]
            item += b_item_image(0, k2_value - p2, column, row, pivot_row, pivot_column, image_matrixes) * pivot_value
        return (d_item_image(0, k2_value, column, row, pivot_row, pivot_column, image_matrixes) - item) / a_i_0_j_0

    if k1_value != 0 and k2_value == 0:
        for p1 in range(1, k1_value + 1):
            pivot_value = image_matrixes[p1][0][pivot_row][pivot_column]
            item += b_item_image(k1_value - p1, 0, column, row, pivot_row, pivot_column, image_matrixes) * pivot_value
        return (d_item_image(k1_value, 0, column, row, pivot_row, pivot_column, image_matrixes) - item) / a_i_0_j_0

    for p1 in range(1, k1_value + 1):
        for p2 in range(1, k2_value + 1):
            pivot_value = image_matrixes[p1][p2][pivot_row][pivot_column]
            item += b_item_image(k1_value - p1, k2_value - p2, column, row, pivot_row, pivot_column,
                                 image_matrixes) * pivot_value

    return (d_item_image(k1_value, k2_value, column, row, pivot_row, pivot_column, image_matrixes) - item) / a_i_0_j_0


# generate next image table
def next_image_table(image_matrixes, pivot_row, pivot_column, k1_value, k2_value):
    table = deepcopy(image_matrixes[0][0])
    columns = len(table[0])
    rows = len(table)

    pivot_value = table[pivot_row][pivot_column]

    pivot_vector = [0 for x in range(columns)]
    for j in range(0, columns):
        pivot_vector[j] = table[pivot_row][j] / pivot_value
        table[pivot_row][j] = pivot_vector[j]

    ratios = [0 for x in range(rows)]
    for i in range(0, rows):
        ratio = table[i][pivot_column]
        ratios[i] = ratio

        if i == pivot_row:
            continue
        for j in range(0, columns):
            multiplier = pivot_vector[j] * ratio
            table[i][j] -= multiplier

    new_image_matrix = deepcopy(image_matrixes)
    # [[0][0] * (k1_value + 1) for x in range(k2_value + 1)]

    # images pivot row values
    for k1 in range(0, k1_value + 1):
        for k2 in range(0, k2_value + 1):
            s_image = [[0.0] * columns for x in range(rows)]

            pivot_image = [0 for x in range(columns)]
            for j in range(0, columns):
                s_image[pivot_row][j] = get_div_image(k1, k2, j, pivot_row, pivot_column, image_matrixes)
                # s_image[pivot_row][j] / pivot_value
            # image_matrixes[k] = s_image

            for i in range(0, rows):
                if i == pivot_row:
                    continue
                for j in range(0, columns):
                    item = (
                    image_matrixes[k1][k2][i][j] - b_item_image(k1, k2, j, i, pivot_row, pivot_column, image_matrixes))
                    s_image[i][j] = item
                    # pivot_image[j] * ratios[i]
            new_image_matrix[k1][k2] = s_image
            print("k1 ======= ", k1, "k2 ======= ", k2)
            printTableu(s_image)
            with open("Output.txt", "a") as text_file:
                print("k1 ======= ", str(k1), "k2 ======= ", str(k2), file=text_file)
            write_table_file(s_image)

    return new_image_matrix


def initiate_simplex_matrix(s_matrix, v_recovered, strategies_recovered, parametric_array, k1_value, k2_value, d_value,
                            t_value):
    with open("Output.txt", "w") as text_file:
        print('--------- Multiparametric GAME MODEL SOLUTION -------------', file=text_file)

    image_matrixes = get_image_matrixes(s_matrix, k1_value, k2_value, t_value, d_value)
    simplex_matrix = prepare_matrix_for_simplex(s_matrix, 0, 0, t_value, d_value)
    printTableu(simplex_matrix)
    image_matrixes = simplex_multi(simplex_matrix, image_matrixes, k1_value, k2_value)

    return image_matrixes


k1_value = 2
k2_value = 2
d_value = 0
t_value = 0

s_matrix = [[1 + t, 2 * d, 1],
            [3 - 2 * t, d, 2],
            [1 + 3 * t, 4, d]]

solution_matrix = initiate_simplex_matrix(s_matrix, [], [], [], k1_value, k2_value, d_value, t_value)

rows = len(s_matrix)

x_parametric_array = [0 for x in range(rows)]
y_parametric_array = [0 for x in range(rows)]

z_parametric_array = [0 for x in range(rows * 2)]

function_max_parametric = 0
for k1 in range(0, k1_value + 1):
    for k2 in range(0, k2_value + 1):
        current_image_table = solution_matrix[k1][k2]
        table_len = len(current_image_table[0])
        for i in range(rows):
            indice = int((table_len - 1) / 2) + 1
            y_parametric_array[i] += current_image_table[0][indice + i] * ((t - t_value) ** k1) * ((d - d_value) ** k2)
            item = current_image_table[i][0]
            x_parametric_array[i - 1] += item * ((t - t_value) ** k1) * ((d - d_value) ** k2)

        for j in range(1, table_len):
            z_parametric_array[j - 1] += current_image_table[0][j] * ((t - t_value) ** k1) * ((d - d_value) ** k2)

        f_image = current_image_table[0][0]
        function_max_parametric += f_image * ((t - t_value) ** k1) * ((d - d_value) ** k2)

print(' parametric F max = ', function_max_parametric)
game_value = 1 / function_max_parametric
print(' parametric Game value = ', game_value)
print(' parametric Game value = ', game_value.evalf(subs={t: t_value, d: d_value}))


print(' parametric x = ', x_parametric_array)
print(' parametric y = ', y_parametric_array)

x_probability = [x * game_value for x in x_parametric_array]
y_probability = [x * game_value for x in y_parametric_array]