from Simplex_Mher import *
from ParametricRightPart import *

t = Symbol('t')
k = 2
t_value = 1


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
    v_recovered = 0
    v_parametric = 0

    x_b_image_matrix = [[0] * len(right_vector) for x in range(k + 1)]
    for i in range(0, k + 1):
        for j in range(0, len(right_vector)):
            image_vec = differential_vector(right_vector, i)
            x_b_image_matrix[i][j] = image_vec[j]

    simplex_matrix = prepare_matrix_for_simplex(s_matrix, right_vector, 0)
    tableu = parametric_simplex(simplex_matrix, x_b_image_matrix)

    printTableu(x_b_image_matrix)

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

    return v_parametric



x_b = [1 + 0.1504*(1 - t), 1 + 0.1504*(1 - t), 1 + 0.1504*(1 - t)]
x1 = [[179.95, 156.12, 90],
      [89.95, 179.87, 155],
      [180, 156, 177]]

strategies_recovered = [0 for x in range(len(x1))]
parametric_array = [0 for x in range(len(x1))]

parametric_simplex_solution(x1, x_b, k, t_value, strategies_recovered, parametric_array)

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
