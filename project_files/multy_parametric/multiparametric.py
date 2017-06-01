from project_files.services.simplex_basic import *
from project_files.services.transformation_util import *
from copy import copy, deepcopy

d = Symbol('d')
t = Symbol('t')
# k = 2
# d_value = 0.5
# t_value = 1.55

w1 = 0.4
w2 = 0.4
w3 = 0.4


R_matrix = [[(0.4 * ((7/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((7.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((4/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((4.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((13.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((7.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((8/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((8.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((10/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((10.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((4/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((4.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((13/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((12.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((9.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((4/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((4.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((10/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((10.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((14.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((9.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((5/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((7.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((10.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((15/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((15.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((10/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((10.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((8/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((7.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((11/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((7.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((4.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((17/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((13.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((8/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((13/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((17.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((4/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((5.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((7.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((4/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((13.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((7.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((12/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((12.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((7.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((14.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((9.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((4/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((14.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((15/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((15.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((10.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((8/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.3/d)** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((14.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((7.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((13.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((18/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((18.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((7.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((9/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((9.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((16/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((15.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((15.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((17/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((17.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((13/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((13.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((8/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((7/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((7.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((3/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((2.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((9.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((13.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((8/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((7.3/d) ** 2)) ** -0.5 ]]

s_matrix = [[1 + t, 2*d, 1],
       [3 - 2*t, d, 2],
       [1 + 3*t, 4, d]]


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

    image_matrixes = [simplex_matrix * (k2_value + 1) for x in range(k1_value + 1)]
    for i in range(0, k1_value + 1):
        for j in range(0, k2_value + 1):
            image_matrixes[i][j] = prepare_matrix_for_simplex(s_matrix, i, j, t_value, d_value)
    return image_matrixes


def simplex_multi(table, image_matrixes, k1_value, k2_value, basis_vector):

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

        basis_vector[pivot_row - 1] = pivot_column

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
            item += get_div_image(k1_value - p1, k2_value - p2, j, pivot_row, pivot_column, image_matrixes) * pivot_value

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
            item += b_item_image(k1_value - p1, k2_value - p2, column, row, pivot_row, pivot_column, image_matrixes) * pivot_value

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
                    item = (image_matrixes[k1][k2][i][j] - b_item_image(k1, k2, j, i, pivot_row, pivot_column, image_matrixes))
                    s_image[i][j] = item
                    # pivot_image[j] * ratios[i]
            new_image_matrix[k1][k2] = s_image
            print("k1 ======= ", k1, "k2 ======= ", k2)
            printTableu(s_image)
            with open("Output.txt", "a") as text_file:
                print("k1 ======= ", str(k1), "k2 ======= ", str(k2), file=text_file)
            write_table_file(s_image)

    return new_image_matrix


def initiate_simplex_matrix(s_matrix, v_recovered, strategies_recovered, parametric_array, k1_value, k2_value, d_value, t_value, basis_vector):

    with open("Output.txt", "w") as text_file:
        print('--------- Multiparametric GAME MODEL SOLUTION -------------', file=text_file)
  
    image_matrixes = get_image_matrixes(s_matrix, k1_value, k2_value, d_value, t_value)
    simplex_matrix = prepare_matrix_for_simplex(s_matrix, 0, 0, t_value, d_value)
    printTableu(simplex_matrix)
    image_matrixes = simplex_multi(simplex_matrix, image_matrixes, k1_value, k2_value, basis_vector)

    return image_matrixes

