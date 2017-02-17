# https://docs.scipy.org/doc/scipy-0.18.1/reference/tutorial/optimize.html#constrained-minimization-of-multivariate-scalar-functions-minimize
from simplex_basic import *
from transformation_util import *
from optimization_util import *
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


def prepare_matrix_for_simplex(s_matrix, right_vector, z_array, i, t_value):
    simplex_matrix = []
    _length = len(s_matrix)
    z = []
    z.append(0.0)
    for z_i in range(0, _length):
        z.append(-z_array[z_i])
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
def parametric_simplex(table, x_image, basis_vector):

    columns = len(table[0])
    rows = len(table) - 1

    array = table[0]
    pivot_column = find_entering_column(array)
    pivot_row = find_departing_row(table, pivot_column)

    print("pivot column", pivot_column)
    print("pivot row", pivot_row)

    write_table_file(table)

    while pivot_column >= 0:
        table = next_image_table(table, x_image, pivot_row, pivot_column)
        printTableu(table)
        write_table_file(table)

        basis_vector[pivot_row - 1] = pivot_column

        if not any([n for n in array if n < 0]):
            break

        array = table[0]
        pivot_column = find_entering_column(array)
        pivot_row = find_departing_row(table, pivot_column)

    return table


def get_parametric_array(x_b_image_matrix, vec_len, k_, t_value, basis_vector):
    parametric_array = [0 for x in range(vec_len)]
    for i in range(0, k + 1):
        for j in range(0, vec_len):
            s_item = x_b_image_matrix[i][j] * ((t-t_value)**i)
            parametric_array[j] += s_item

    printTableu(x_b_image_matrix)
    # game_parametric = 1/sum(parametric_array)

    print(parametric_array)
    # print(game_parametric)

    return parametric_array


def parametric_simplex_solution(s_matrix, right_vector, z_array, k_, t_value_):
    k = k_
    t_value = t_value_

    solution = []
    step_array = []
    has_solution = true

    with open("Output.txt", "w") as text_file:
        print('--------- GAME MODEL SOLUTION -------------', file=text_file)

    while has_solution:

        x_b_image_matrix = [[0] * len(right_vector) for x in range(k + 1)]
        for i in range(0, k + 1):
            for j in range(0, len(right_vector)):
                image_vec = differential_vector(right_vector, i, t_value)
                x_b_image_matrix[i][j] = image_vec[j]

        right_len = len(right_vector)
        basis_vector = [0 for x in range(right_len)]
        for j in range(right_len):
            basis_vector[j] = right_len + j + 1

        simplex_matrix = prepare_matrix_for_simplex(s_matrix, right_vector, z_array, 0, t_value)
        tableu = parametric_simplex(simplex_matrix, x_b_image_matrix, basis_vector)

        try:
            new_max = nonlinear_optimality(x_b_image_matrix, k, len(right_vector), t_value)
            if math.isnan(float(new_max)):
                break
            if new_max > t_value:
                step_array.append(t_value)
                step_array.append(new_max)
                step_array.append(x_b_image_matrix)
                step_array.append(basis_vector)
                solution.append(step_array)
                step_array = []
                t_value = new_max
            else:
                break
        except TypeError:
            has_solution = false

    return solution


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

