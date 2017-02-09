from transformation_util import *
from simplex_basic import *


d = Symbol('d')
t = Symbol('t')
# k = 2
# d_value = 0.02
# t_value = 1.55


R_matrix = [[(0.4 * (7/d ** 2) + 0.4 * (0.7/t ** 2) + 0.4 * (7.1/d ** 2)) ** -1/2,
             (0.4 * (4/d ** 2) + 0.4 * (0.5/t ** 2) + 0.4 * (4.2/d ** 2)) ** -1/2,
             (0.4 * (6/d ** 2) + 0.4 * (0.6/t ** 2) + 0.4 * (6.3/d ** 2)) ** -1/2,
             (0.4 * (11/d ** 2) + 0.4 * (1.6/t ** 2) + 0.4 * (11.1/d ** 2)) ** -1/2,
             (0.4 * (5/d ** 2) + 0.4 * (0.6/t ** 2) + 0.4 * (5.4/d ** 2)) ** -1/2],

            [(0.4 * (8/d ** 2) + 0.4 * (0.7/t ** 2) + 0.4 * (8.1/d ** 2)) ** -1/2,
             (0.4 * (10/d ** 2) + 0.4 * (0.5/t ** 2) + 0.4 * (10.2/d ** 2)) ** -1/2,
             (0.4 * (6/d ** 2) + 0.4 * (0.6/t ** 2) + 0.4 * (6.3/d ** 2)) ** -1/2,
             (0.4 * (4/d ** 2) + 0.4 * (1.6/t ** 2) + 0.4 * (4.1/d ** 2)) ** -1/2,
             (0.4 * (5/d ** 2) + 0.4 * (0.6/t ** 2) + 0.4 * (5.4/d ** 2)) ** -1/2],

            [(0.4 * (4/d ** 2) + 0.4 * (0.7/t ** 2) + 0.4 * (4.1/d ** 2)) ** -1/2,
             (0.4 * (10/d ** 2) + 0.4 * (0.5/t ** 2) + 0.4 * (10.2/d ** 2)) ** -1/2,
             (0.4 * (6/d ** 2) + 0.4 * (0.6/t ** 2) + 0.4 * (6.3/d ** 2)) ** -1/2,
             (0.4 * (14/d ** 2) + 0.4 * (1.6/t ** 2) + 0.4 * (14.1/d ** 2)) ** -1/2,
             (0.4 * (5/d ** 2) + 0.4 * (0.6/t ** 2) + 0.4 * (5.4/d ** 2)) ** -1/2],

            [(0.4 * (5/d ** 2) + 0.4 * (0.7/t ** 2) + 0.4 * (7.1/d ** 2)) ** -1/2,
             (0.4 * (9/d ** 2) + 0.4 * (0.5/t ** 2) + 0.4 * (10.2/d ** 2)) ** -1/2,
             (0.4 * (15/d ** 2) + 0.4 * (0.6/t ** 2) + 0.4 * (15.3/d ** 2)) ** -1/2,
             (0.4 * (11/d ** 2) + 0.4 * (1.6/t ** 2) + 0.4 * (11.1/d ** 2)) ** -1/2,
             (0.4 * (10/d ** 2) + 0.4 * (0.6/t ** 2) + 0.4 * (10.4/d ** 2)) ** -1/2],

            [(0.4 * (11/d ** 2) + 0.4 * (0.7/t ** 2) + 0.4 * (7.1/d ** 2)) ** -1/2,
             (0.4 * (14/d ** 2) + 0.4 * (0.5/t ** 2) + 0.4 * (4.2/d ** 2)) ** -1/2,
             (0.4 * (6/d ** 2) + 0.4 * (0.6/t ** 2) + 0.4 * (6.3/d ** 2)) ** -1/2,
             (0.4 * (11/d ** 2) + 0.4 * (1.6/t ** 2) + 0.4 * (11.1/d ** 2)) ** -1/2,
             (0.4 * (5/d ** 2) + 0.4 * (0.6/t ** 2) + 0.4 * (5.4/d ** 2)) ** -1/2]]


def printTableu(tableu):
 print('----------------------')
 for row in tableu:
  print (row)
 print('----------------------')
 return


def item_multi_transform(item, t_level, d_level, value, d_value):
    if t_level == 0:
        return item.evalf(subs={t: value, d: d_value})
    derivative = diff(item, t, t_level)
    d_derive = diff(derivative, d, d_level)
    expr_with_value = d_derive.evalf(subs={t: value, d: d_value})
    return expr_with_value / factorial(t_level)


def matrix_multi_differential(matrix, t_level, d_level, t_value, d_value):
    "returns a differential of given matrix"
    _length = len(matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for i in range(0, _length):
        for j in range(0, _length):
            z_matrix[i][j] = item_multi_transform(matrix[i][j], t_level, d_level, t_value, d_value)
    return z_matrix


def prepare_matrix_for_simplex(R_matrix, i, j, t_value, d_value):
    simplex_matrix = []
    _length = len(R_matrix)
    z = []
    z.append(0.0)
    for z_i in range(0, _length):
        z.append(-1.0)
    for z_i in range(0, _length):
        z.append(0.0)
    simplex_matrix.append(z)
    base_matrix = matrix_multi_differential(R_matrix, i, j, t_value, d_value)
    for m_i in range(0, _length):
        m_array = [0 for var in range(_length * 2 + 1)]
        for m_j in range(0, _length):
            m_array[0] = 1.0
            m_array[m_j + 1] = base_matrix[m_i][m_j]
            if m_i == m_j:
                m_array[_length + m_j + 1] = 1.0
            else:
                m_array[_length + m_j + 1] = 0.0
        simplex_matrix.append(m_array)
    return simplex_matrix


def get_image_matrixes(s_matrix, k1_value, k2_value, d_value, t_value):
    _length = len(s_matrix)
    z_matrix = [[0] * _length for x in range(_length)]

    image_matrixes = [z_matrix * (k1_value + 1) for x in range(k2_value + 1)]
    for i in range(0, k1_value + 1):
        for j in range(0, k2_value + 1):
            image_matrixes[i][j] = matrix_multi_differential(s_matrix, i, j, d_value, t_value)
    return image_matrixes


def simplex_multi(table, image_matrixes, k1_value, k2_value):

    columns = len(table[0])
    rows = len(table) - 1

    array = table[0]
    pivot_column = find_entering_column(array)
    pivot_row = find_departing_row(table, pivot_column)

    print("pivot column", pivot_column)
    print("pivot row", pivot_row)

    while pivot_column >= 0:
        table = next_image_table(table, pivot_row, pivot_column)

        for k1 in range(0, k1_value + 1):
            for k2 in range(0, k2_value + 1):
                # pivot image row
                image_matrix = image_matrixes[k1][k2]
                next_image_table(image_matrix, pivot_row, pivot_column)
                image_matrixes[k1][k2] = image_matrix

        printTableu(table)

        if not any([n for n in array if n < 0]):
            break

        array = table[0]
        pivot_column = find_entering_column(array)
        pivot_row = find_departing_row(table, pivot_column)

    return table


def next_image_table(table, pivot_row, pivot_column):

    columns = len(table[0])
    rows = len(table)

    pivot_value = table[pivot_row][pivot_column]

    # pivot row
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


def initiate_simplex_matrix(s_matrix, v_recovered, strategies_recovered, parametric_array, k1_value, k2_value, d_value, t_value):

    image_matrixes = get_image_matrixes(s_matrix, k1_value, k2_value, t_value, d_value)
    simplex_matrix = prepare_matrix_for_simplex(image_matrixes[0][0], k1_value, k2_value, t_value, d_value)
    tableu = simplex_multi(simplex_matrix, image_matrixes, k1_value, k2_value)

    printTableu(simplex_matrix)


#print(R_matrix)
# print('---------------------------------------------------------------------------------')
# print(item_multi_transform((0.4 * (6/d ** 2) + 0.4 * (0.6/t ** 2) + 0.4 * (7.3/d ** 2)) ** -1/2, 0, 1, 0.5, 0.03))
# print('---------------------------------------------------------------------------------')
# differentiated = matrix_multi_differential(R_matrix, 0, 0, t_value, d_value)
#print(differentiated)
# print(matrix_multi_differential(R_matrix, 1, 2, 0.5, 0.03))

# initiate_simplex_matrix(R_matrix)

z = [0.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0,  0.0,  0.0,  0.0,  0.0]
x1 = [1.0,  (0.4 * (1.2 ** 2) + 0.4 * (0.3 ** 2) + 0.4 * (1.1 ** 2)) ** -1/2,  (0.4 * (1.2 ** 2) + 0.4 *(0.11 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2, (0.4 * (1.2 ** 2) + 0.4 *(0.1 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2,  (0.4 * (1.2 ** 2) + 0.4 *(0.12 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2, (0.4 * (1.2 ** 2) + 0.4 *(0.31 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2,  1.0,  0.0,  0.0,  0.0,  0.0]
x2 = [1.0, (0.4 * (1.4 ** 2) + 0.4 * (0.2 ** 2) + 0.4 * (1.0 ** 2)) ** -1/2, (0.4 * (0.7 ** 2) + 0.4 *(0.2 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2, (0.4 * (1.2 ** 2) + 0.4 *(0.31 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2, (0.4 * (1.2 ** 2) + 0.4 *(0.17 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2, (0.4 * (1.2 ** 2) + 0.4 *(0.12 ** 2) + 0.4 *(0.1 ** 2)) ** -1/2,   0.0,  1.0,  0.0,  0.0,  0.0]
x3 = [1.0,  (0.4 * (1.2 ** 2) + 0.4 * (0.11 ** 2) + 0.4 * (1.15 ** 2)) ** -1/2,  (0.4 * (0.9 ** 2) + 0.4 *(0.17 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2, (0.4 * (1.2 ** 2) + 0.4 *(0.14 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2, (0.4 * (0.9 ** 2) + 0.4 *(0.24 ** 2) + 0.4 *(1.2 ** 2)) ** -1/2, (0.4 * (1.2 ** 2) + 0.4 *(0.18 ** 2) + 0.4 *(1.3 ** 2)) ** -1/2,  0.0,  0.0,  1.0,  0.0,  0.0]
x4 = [1.0,  (0.4 * (1.1 ** 2) + 0.4 * (0.16 ** 2) + 0.4 * (1.14 ** 2)) ** -1/2,  (0.4 * (1.2 ** 2) + 0.4 *(0.25 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2, (0.4 * (1.2 ** 2) + 0.4 *(0.2 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2,  (0.4 * (1.2 ** 2) + 0.4 *(0.23 ** 2) + 0.4 *(1.4 ** 2)) ** -1/2, (0.4 * (1.2 ** 2) + 0.4 *(0.26 ** 2) + 0.4 *(1.0 ** 2)) ** -1/2,  0.0,  0.0,  0.0,  1.0,  0.0]
x5 = [1.0,  (0.4 * (1.6 ** 2) + 0.4 * (0.21 ** 2) + 0.4 * (1.2 ** 2)) ** -1/2,  (0.4 * (1.2 ** 2) + 0.4 *(0.3 ** 2) + 0.4 * (1.1 ** 2)) ** -1/2, (0.4 * (1.2 ** 2) + 0.4 *(0.21 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2,  (0.4 * (0.7 ** 2) + 0.4 *(0.12 ** 2) + 0.4 *(0.3 ** 2)) ** -1/2, (0.4 * (1.2 ** 2) + 0.4 *(0.2 ** 2) + 0.4 *(0.9 ** 2)) ** -1/2,  0.0,  0.0,  0.0,  0.0,  1.0]


print('---------------------------------------------------------------------')
# print((0.4 * (9.2 ** 2) + 0.4 * (9.1 ** 2) + 0.4 * (28 ** 2)) ** -1/2)
# print((0.4 * (1.2 ** 2) + 0.4 * (0.7 ** 2) + 0.4 * (1.1 ** 2)) ** -1/2)

# 0.00399470416362308, 0.00825736557008852, 0.00450694068866054, 0.00356068293898770,
# 0.00619834710743802, 0.000923361034164358, 0.00226421929718633, 0.00631259994949920, 0.00131300222335043, 0.00388178665700533


p_item = 0.0003*((t-0.2)**0)*((d-0.5)**0) + 0.0011*((t-0.2)**1)*((d-0.5)**1) + 0.0002*((t-0.2)**2)*((d-0.5)**2) + 0.00016*((t-0.2)**0)*((d-0.5)**1)
p_item1 = 0.0001*((t-0.2)**0)*((d-0.5)**2) + 0.00024*((t-0.2)**1)*((d-0.5)**0) + 0.0038*((t-0.2)**2)*((d-0.5)**0)
p_item2 = 0.0034*((t-0.2)**1)*((d-0.5)**2) + 0.0085*((t-0.2)**2)*((d-0.5)**1)
result = p_item + p_item1 + p_item2
#print(result)
#print(result.evalf(subs={t: 0.5, d: 0.2}))
