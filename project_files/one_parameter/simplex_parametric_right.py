# https://docs.scipy.org/doc/scipy-0.18.1/reference/tutorial/optimize.html#constrained-minimization-of-multivariate-scalar-functions-minimize
from project_files.services.optimization_util import *
from project_files.services.simplex_basic import *
from copy import copy, deepcopy

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


def prepare_matrix_for_simplex(s_matrix, right_vector, z_array, k_value, t_value):
    simplex_matrix = []
    _length = len(s_matrix)
    z = []
    z.append(0.0)
    for z_i in range(0, _length):
        if k_value == 0:
            z.append(-z_array[z_i])
        else:
            z.append(0.0)
    for z_i in range(0, _length):
        z.append(0.0)
    simplex_matrix.append(z)
    vector_diff = differential_vector(right_vector, k_value, t_value)
    s_diff = matrix_differential(s_matrix, k_value, t_value)
    for m_i in range(0, _length):
        m_array = [0 for var in range(_length * 2 + 1)]
        for m_j in range(0, _length):
            m_array[0] = vector_diff[m_i]
            m_array[m_j + 1] = s_diff[m_i][m_j]
            if m_i == m_j and k_value == 0:
                m_array[_length + m_j + 1] = 1.0
            else:
                m_array[_length + m_j + 1] = 0.0
        simplex_matrix.append(m_array)
    return simplex_matrix


# get division image value
def get_div_image(k_value, j, pivot_row, pivot_column, image_matrixes):
    item = 0

    a_i_0_j_0 = image_matrixes[0][pivot_row][pivot_column]

    if k_value == 0:
        return image_matrixes[0][pivot_row][j] / a_i_0_j_0

    for p in range(1, k_value + 1):
        pivot_value = image_matrixes[p][pivot_row][pivot_column]
        item += get_div_image(k_value - p, j, pivot_row, pivot_column, image_matrixes) * pivot_value

    return (image_matrixes[k_value][pivot_row][j] - item) / a_i_0_j_0


def d_item_image(k_value, column, row, pivot_row, pivot_column, image_matrixes):
    d_item = 0

    for p in range(1, k_value + 1):
        row_0 = image_matrixes[k_value - p][pivot_row][column]
        col_0 = image_matrixes[p][row][pivot_column]
        d_item += row_0 * col_0

    return d_item


def b_item_image(k_value, column, row, pivot_row, pivot_column, image_matrixes):
    item = 0

    a_i_0_j_0 = image_matrixes[0][pivot_row][pivot_column]

    if k_value == 0:
        return d_item_image(0, column, row, pivot_row, pivot_column, image_matrixes) / a_i_0_j_0
    for p in range(1, k_value + 1):
        pivot_value = image_matrixes[p][pivot_row][pivot_column]
        item += b_item_image(k_value - p, column, row, pivot_row, pivot_column, image_matrixes) * pivot_value

    return (d_item_image(k_value, column, row, pivot_row, pivot_column, image_matrixes) - item) / a_i_0_j_0


# generate next image table
def next_image_table(image_matrixes, x_image, pivot_row, pivot_column):

    table = image_matrixes[0]
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

    k_count = len(image_matrixes)

    new_image_matrix = []

    # images pivot row values
    for k in range(0, k_count):
        s_image = deepcopy(image_matrixes[k])

        pivot_image = [0 for x in range(columns)]
        for j in range(0, columns):
            pivot_image[j] = get_div_image(k, j, pivot_row, pivot_column, image_matrixes)
            # s_image[pivot_row][j] / pivot_value
            s_image[pivot_row][j] = pivot_image[j]
        # image_matrixes[k] = s_image

        for i in range(0, rows):
            if i == pivot_row:
                continue
            for j in range(0, columns):
                s_image[i][j] -= b_item_image(k, j, i, pivot_row, pivot_column, image_matrixes)
                # pivot_image[j] * ratios[i]
        new_image_matrix.append(s_image)
        print("k = ", k)
        printTableu(s_image)
    image_matrixes = new_image_matrix
    return image_matrixes


#main simplex method
def parametric_simplex(table, image_matrixes, x_image, basis_vector):

    array = table[0]
    pivot_column = find_entering_column(array)
    pivot_row = find_departing_row(table, pivot_column)

    print("pivot column", pivot_column)
    print("pivot row", pivot_row)

    write_table_file(table)

    while pivot_column >= 0:
        image_matrixes = next_image_table(image_matrixes, x_image, pivot_row, pivot_column)

        basis_vector[pivot_row - 1] = pivot_column

        if not any([n for n in array if n < 0]):
            break

        table = image_matrixes[0]
        array = table[0]
        pivot_column = find_entering_column(array)
        pivot_row = find_departing_row(table, pivot_column)

    return image_matrixes


def get_parametric_array(image_matrixes, vec_len, k_value, t_value, basis_vector):
    parametric_array = [0 for x in range(vec_len)]
    for k in range(0, k_value + 1):
        image_matrix = image_matrixes[k]
        rows = len(image_matrix)
        for j in range(1, rows):
            s_item = image_matrix[j][0] * ((t-t_value)**k)
            parametric_array[j - 1] += s_item

    # printTableu(x_b_image_matrix)
    # game_parametric = 1/sum(parametric_array)

    print(parametric_array)
    # print(game_parametric)

    return parametric_array


def matrix_differential(matrix, k_level, t_value):
    "returns a differential of given matrix"
    _length = len(matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for i in range(0, _length):
        for j in range(0, _length):
            if is_number(matrix[i][j]):
                if k_level == 0:
                    z_matrix[i][j] = matrix[i][j]
                else:
                    z_matrix[i][j] = 0
            else:
                 z_matrix[i][j] = item_transform(matrix[i][j], k_level, t_value)
    return z_matrix


def get_image_matrixes(s_matrix, right_vector, z_array, k_value, t_value):
    image_matrixes = []
    for i in range(0, k_value + 1):
        image_matrixes.append(prepare_matrix_for_simplex(s_matrix, right_vector, z_array, i, t_value))

    for i in range(0, k_value + 1):
        printTableu(image_matrixes[i])
    return image_matrixes


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

        try:
            image_matrixes = get_image_matrixes(s_matrix, right_vector, z_array, k, t_value)
            simplex_matrix = prepare_matrix_for_simplex(s_matrix, right_vector, z_array, 0, t_value)
            image_matrixes = parametric_simplex(simplex_matrix, image_matrixes, x_b_image_matrix, basis_vector)
            # image_matrixes[0] = tableu
            new_max = x_b_nonlinear_optimality(image_matrixes, k, len(right_vector), t_value)

            z_max = z_nonlinear_optimality(image_matrixes, x_b_image_matrix, k, len(right_vector), t_value)

            if math.isnan(float(new_max)) and math.isnan(float(z_max)):
                break

            compare_value = t_value

            if not math.isnan(float(new_max)):
                compare_value = new_max

            if not math.isnan(float(z_max)):
                compare_value = z_max

            if (not math.isnan(float(z_max))) and (not math.isnan(float(new_max))) and new_max > z_max > t_value:
                compare_value = z_max

            if compare_value > t_value:
                step_array.append(t_value)
                step_array.append(compare_value)
                step_array.append(image_matrixes)
                step_array.append(basis_vector)
                solution.append(step_array)
                step_array = []
                t_value = compare_value
            else:
                break
        except TypeError:
            has_solution = false
        except ValueError:
            has_solution = false

    image_matrixes = []
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

