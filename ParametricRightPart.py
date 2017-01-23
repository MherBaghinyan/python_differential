from TransformationUtils import *
from simplex import *

t = Symbol('t')
k = 2
t_value = 1

#  max r1 + r2 + r3

#  179.95r1 + 156.12r2 + 90r3 ≤ 1 + 0.1504(1 − α)

#  89.95r1 + 179.87r2 + 155r3 ≤ 1 + 0.1504(1 − α)

#  180r1 + 156r2 + 177r3 ≤ 1 + 0.1504(1 − α)

#  r1, r2, r3 ≥ 0, α ∈]0, 1].


# def matrix_differential(matrix, t_level, t_value):
#     "returns a differential of given matrix"
#     _length = len(matrix)
#     z_matrix = [[0] * _length for x in range(_length)]
#     for i in range(0, _length):
#         for j in range(0, _length):
#             z_matrix[i][j] = item_transform(matrix[i][j], t_level, t_value)
#     return z_matrix


def prepare_matrix_for_simplex(s_matrix, right_vector, i):
    simplex_matrix = []
    _length = len(s_matrix)
    z = []
    z.append(0.0)
    for z_i in range(0, _length):
        z.append(-1.0)
    for z_i in range(0, _length):
        z.append(0.0)
    simplex_matrix.append(z)
    vector_diff = differential_vector(right_vector, i)
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


def initiate_simplex_matrix(s_matrix, right_vector, k_, t_value_, strategies_recovered, parametric_array):

    k = k_
    t_value = t_value_
    v_recovered = 0
    v_parametric = 0
    for i in range(0, k + 1):
        simplex_matrix = prepare_matrix_for_simplex(s_matrix, right_vector, i)
        tableu = simplex(simplex_matrix)
        V = 0
        if tableu[0][0] != 0:
            V = 1 / tableu[0][0]
        print("V = ", V)
        length = len(tableu)
        strategies = [0 for x in range(length - 1)]
        for n in range(1, length):
            strategies[n - 1] = tableu[n][0]
        # print(tableu[n][0])
        # print(strategies)

        item = V*((t-t_value)**i)
        v_parametric += item
        v_recovered += item.evalf(subs={t: t_value})
        for n in range(0, length - 1):
            s_item = strategies[n] * ((t-t_value)**i)
            parametric_array[n] += s_item
            strategies_recovered[n] += s_item.evalf(subs={t: t_value})
        # print(simplex_matrix)
        # print('----------------', i)
        #
        # print(v_recovered)
        # print(strategies_recovered)

    print(strategies_recovered)
    print(parametric_array)
    print('parametric v', v_parametric)
    print()
    return v_parametric


# x_b = [1 + 0.1504*(1 - t), 1 + 0.1504*(1 - t), 1 + 0.1504*(1 - t)]
# x1 = [[179.95, 156.12, 90],
#       [89.95, 179.87, 155],
#       [180, 156, 177]]

# v_recovered = initiate_simplex_matrix(x1, x_b, strategies_recovered, parametric_array)

