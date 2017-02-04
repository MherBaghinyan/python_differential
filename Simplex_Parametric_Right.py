from simplex_basic import *
from transformation_util import *

t = Symbol('t')
k = 2
t_value = 0


def optimality_matrix_for_simplex(s_matrix):
    simplex_matrix = []
    _length = len(s_matrix[0])
    z = []
    z.append(0.0)
    z.append(-1.0)
    for z_i in range(0, _length):
        z.append(0.0)
    simplex_matrix.append(z)

    m_j = 1
    for m_i in range(0, _length):
        m_array = [0.0 for var in range(_length + 2)]
        m_array[0] = s_matrix[0][m_i]
        m_array[1] = -s_matrix[1][m_i]
        m_array[1 + m_j] = 1.0
        m_j += 1
        simplex_matrix.append(m_array)
    return simplex_matrix


def prepare_matrix_for_simplex(s_matrix, right_vector, i, t_value):
    simplex_matrix = []
    _length = len(s_matrix)
    z = []
    z.append(0.0)
    for z_i in range(0, _length):
        z.append(-1.0)
    for z_i in range(0, _length):
        z.append(0.0)
    simplex_matrix.append(z)
    vector_diff = differential_vector(right_vector, i, t_value)
    for m_i in range(0, _length):
        m_array = [0 for var in range(_length * 2 + 1)]
        for m_j in range(0, _length):
            m_array[0] = vector_diff[m_i]
            m_array[m_j + 1] = s_matrix[m_i][m_j]
            if m_i == m_j:
                m_array[_length + m_j + 1] = 1.0
            else:
                m_array[_length + m_j + 1] = 0.0
        simplex_matrix.append(m_array)
    return simplex_matrix


# generate next image table
def next_image_table(table, x_image, pivot_row, pivot_column):

    columns = len(table[0])
    rows = len(table)

    pivot_value = table[pivot_row][pivot_column]

    pivot_vector = [0 for x in range(columns)]
    for j in range(0, columns):
        pivot_vector[j] = table[pivot_row][j] / pivot_value
        table[pivot_row][j] = pivot_vector[j]

    # Xb images pivot row values
    k_count = len(x_image)
    for k in range(0, k_count):
        x_image[k][pivot_row - 1] /= pivot_value

    ratios = [0 for x in range(rows - 1)]
    for i in range(0, rows):
        ratio = table[i][pivot_column]
        if i != 0:
            ratios[i - 1] = ratio

        if i == pivot_row:
            continue
        for j in range(0, columns):
            multiplier = pivot_vector[j] * ratio
            table[i][j] -= multiplier

    # Xb images pivot row values
    for k in range(0, k_count):
        for i in range(0, rows - 1):
            if i == pivot_row - 1:
                continue
            x_image[k][i] -= x_image[k][pivot_row - 1] * ratios[i]

    return table


#main simplex method
def parametric_simplex(table, x_image):

    columns = len(table[0])
    rows = len(table) - 1

    array = table[0]
    pivot_column = find_entering_column(array)
    pivot_row = find_departing_row(table, pivot_column)

    print("pivot column", pivot_column)
    print("pivot row", pivot_row)

    while pivot_column >= 0:
        table = next_image_table(table, x_image, pivot_row, pivot_column)
        printTableu(table)

        if not any([n for n in array if n < 0]):
            break

        array = table[0]
        pivot_column = find_entering_column(array)
        pivot_row = find_departing_row(table, pivot_column)

    return table


def parametric_simplex_solution(s_matrix, right_vector, k_, t_value_, strategies_recovered, parametric_array):
    k = k_
    t_value = t_value_

    # right_vector =[1 + 0.1504*(1 - t), 1 + 0.1504*(1 - t), 1 + 0.1504*(1 - t)]

    # right_vector = [40 - t, 60 + 2*t, 30 - 7*t]

    x_b_image_matrix = [[0] * len(right_vector) for x in range(k + 1)]
    for i in range(0, k + 1):
        for j in range(0, len(right_vector)):
            image_vec = differential_vector(right_vector, i, t_value)
            x_b_image_matrix[i][j] = image_vec[j]

    simplex_matrix = prepare_matrix_for_simplex(s_matrix, right_vector, 0, t_value)

    # simplex_matrix = [
    #     [0.0, -3, -2, -5, 0.0, 0.0, 0.0],
    #     [40, 1.0, 2.0, 1.0, 1.0, 0.0, 0.0],
    #     [60, 3.0, 0.0, 2.0, 0.0, 1.0, 0.0],
    #     [30, 1.0, 4.0, 0.0, 0.0, 0.0, 1.0]
    # ]

    tableu = parametric_simplex(simplex_matrix, x_b_image_matrix)

    for i in range(0, k + 1):
        for j in range(0, len(right_vector)):
            s_item = x_b_image_matrix[i][j] * ((t-t_value)**i)
            parametric_array[j] += s_item

    printTableu(x_b_image_matrix)
    game_parametric = 1/sum(parametric_array)

    print(parametric_array)
    print(game_parametric)

    for i in range(0, len(parametric_array)):
        print(parametric_array[i].evalf(subs={t: t_value}))

    optimality_matrix = optimality_matrix_for_simplex(x_b_image_matrix)
    o_matrix = simplex_mher(optimality_matrix)
    print(o_matrix)
    # for i in range(0, k + 1):
    #     simplex_matrix = prepare_matrix_for_simplex(s_matrix, right_vector, i)
    #     tableu = simplex(simplex_matrix)
    #     V = 0
    #     if tableu[0][0] != 0:
    #         V = 1 / tableu[0][0]
    #     print("V = ", V)
    #     length = len(tableu)
    #     strategies = [0 for x in range(length - 1)]
    #     for n in range(1, length):
    #         strategies[n - 1] = tableu[n][0]
    #     # print(tableu[n][0])
    #     # print(strategies)
    #
    #     item = V*(t**i)
    #     v_parametric += item
    #     v_recovered += item.evalf(subs={t: t_value})
    #     for n in range(0, length - 1):
    #         s_item = strategies[n] * (t**i)
    #         parametric_array[n] += s_item
    #         strategies_recovered[n] += s_item.evalf(subs={t: t_value})

    return game_parametric



# x_b = [1 + 0.1504*(1 - t), 1 + 0.1504*(1 - t), 1 + 0.1504*(1 - t)]
# x1 = [[179.95, 156.12, 90],
#       [89.95, 179.87, 155],
#       [180, 156, 177]]
#
# strategies_recovered = [0 for x in range(len(x1))]
# parametric_array = [0 for x in range(len(x1))]

# parametric_simplex_solution(x1, x_b, k, t_value, strategies_recovered, parametric_array)

# tableu = []
# z = [0.0, -1.0, -1.0, -1.0, 0.0,  0.0,  0.0]
# x1 = [1.1504, 179.95,  156.12, 90,  1.0,  0.0,  0.0]
# x2 = [1.1504, 89.95, 179.87, 155,   0.0,  1.0,  0.0]
# x3 = [1.1504, 180,  156, 177,  0.0,  0.0,  1.0]
#
# tableu.append(z)
# tableu.append(x1)
# tableu.append(x2)
# tableu.append(x3)
#
# tableu = simplex_mher(tableu)


    # right_vector = [40 - t, 60 + 2*t, 30 - 7*t]
    #
    # simplex_matrix = [
    #     [0.0, -3, -2, -5, 0.0, 0.0, 0.0],
    #     [40, 1.0, 2.0, 1.0, 1.0, 0.0, 0.0],
    #     [60, 3.0, 0.0, 2.0, 0.0, 1.0, 0.0],
    #     [30, 1.0, 4.0, 0.0, 0.0, 0.0, 1.0]
    # ]

