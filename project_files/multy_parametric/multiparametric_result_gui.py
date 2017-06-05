# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from project_files.multy_parametric.multiparametric import *
from project_files.services.graph_gui import *
from project_files.services.optimization_util import *


def multy_window(root, s_matrix, k1_value, k2_value, d_value, t_value):
    mul_root = Toplevel(root)
    mul_root.title("game model solution")
    mul_root.geometry("800x400")

    # k1_value = 2
    # k2_value = 2
    # d_value = 0
    # t_value = 0

    # s_matrix = [[179.95 + t, 156.12*d + t**2, d*(1-0.2*t), 60*t + 5*d],
    #             [89.95 + (d**2 + 1)/2, 160 + 1/d, 90*t + d, 7/t + 58.7],
    #             [155, 120 + 1/(2*t + d), 184 + (d - 1)**2, 120],
    #             [180*t + (d + t), 156 + 5 + d, 77*t**3, 162 + t/(d-7)]]

    # s_matrix = [[179.95 + t, 156.12*d + t**2, d*(1-0.2*t)],
    #             [89.95 + sqrt(d + 1), 160 + 1/d, 90*t + d],
    #             [180*t + (d + t), 156 + 5 + d, 77*t**3]]

    # s_matrix = [[1 + t, 2*d, 1],
    #        [3 - 2*t, d, 2],
    #        [1 + 3*t, 4, d]]

    rows = len(s_matrix)

    basis_vector = [0 for x in range(rows)]
    for j in range(rows):
        basis_vector[j] = rows + j + 1

    solution_matrix = initiate_simplex_matrix(s_matrix, [], [], [], k1_value, k2_value, d_value, t_value, basis_vector)

    x_parametric_array = [0 for x in range(rows)]
    y_parametric_array = [0 for x in range(rows)]

    z_parametric_array = [0 for x in range(rows*2)]

    function_max_parametric = 0
    for k1 in range(0, k1_value + 1):
        for k2 in range(0, k2_value + 1):
            current_image_table = solution_matrix[k1][k2]
            table_len = len(current_image_table[0])
            for i in range(1, rows + 1):
                # indice = int((table_len - 1) / 2) + 1
                # y_parametric_array[i] += current_image_table[0][indice + i]*((t-t_value)**k1)*((d-d_value)**k2)
                item = current_image_table[i][0]
                x_parametric_array[i - 1] += item*((t-t_value)**k1)*((d-d_value)**k2)

            for j in range(1, table_len):
                z_parametric_array[j - 1] += current_image_table[0][j]*((t-t_value)**k1)*((d-d_value)**k2)

            f_image = current_image_table[0][0]
            function_max_parametric += f_image*((t-t_value)**k1)*((d-d_value)**k2)

    print("basis vector", basis_vector)
    for b in range(len(basis_vector)):
        if basis_vector[b] > len(basis_vector):
            x_parametric_array[b] = 0
            basis_vector[b] = 0

    print("basis vector after 0s", basis_vector)
    print(' parametric F max = ', sum(x_parametric_array))
    game_value = 1/sum(x_parametric_array)
    print(' parametric Game value = ', game_value)
    print(' parametric Game value = ', game_value.evalf(subs={t: t_value, d: d_value}))
    # print(' parametric Game value = t, d +0.1', game_value.evalf(subs={t: t_value, d: d_value + 0.1}))
    # print(' parametric Game value = t, d +0.2', game_value.evalf(subs={t: t_value, d: d_value + 0.2}))
    # print(' parametric Game value = t, d +0.3', game_value.evalf(subs={t: t_value, d: d_value + 0.3}))
    # print(' parametric Game value = t, d +0.4', game_value.evalf(subs={t: t_value, d: d_value + 0.4}))
    # print(' parametric Game value = t, d +0.5', game_value.evalf(subs={t: t_value, d: d_value + 0.5}))
    # print(' parametric Game value = t +0.1, d', game_value.evalf(subs={t: t_value + 0.1, d: d_value}))
    # print(' parametric Game value = t +0.2, d', game_value.evalf(subs={t: t_value + 0.2, d: d_value}))
    # print(' parametric Game value = t +0.3, d', game_value.evalf(subs={t: t_value + 0.3, d: d_value}))
    # print(' parametric Game value = t +0.4, d', game_value.evalf(subs={t: t_value + 0.4, d: d_value}))
    # print(' parametric Game value = t +0.5, d', game_value.evalf(subs={t: t_value + 0.5, d: d_value}))
    # print(' parametric Game value = t +1, d +1', game_value.evalf(subs={t: t_value + 1, d: d_value + 1}))

    x_probability = [x * game_value for x in x_parametric_array]
    y_probability = [x * game_value for x in y_parametric_array]

    print(' x_parametric array = ', x_parametric_array)
    # print(' y_parametric array = ', y_parametric_array)
    print(' z_parametric_array array = ', z_parametric_array)
    # print(' y_probability array = ', y_probability)
    print(' x_probability array = ', x_probability)

    res = multy_nonlinear_optimality(x_parametric_array, d_value, t_value)

    # Label(mul_root, text=" - ").grid(row=k1_value + 1, column=1)
    Label(mul_root, text=" Game Value = " + str(game_value)).grid(row=k1_value + 2, column=1)
    Label(mul_root, text=" - ").grid(row=k1_value + 3, column=1)
    Label(mul_root, text=" X probabilities  ").grid(row=k1_value + 4, column=0)
    # Label(mul_root, text=" Y probabilities ").grid(row=k1_value + 4, column=2)

    probability_values = [0 for x in range(len(basis_vector))]
    for i in range(0, len(basis_vector)):
        if basis_vector[i] != 0:
            probability_values[basis_vector[i] - 1] = x_probability[i]

    for k1 in range(0, len(x_probability)):
        # print('y_probability values ', y_probability[k1].evalf(subs={t: t_value, d: d_value}))
        if is_number(probability_values[k1]):
            print('x_probability values = ', probability_values[k1])
        else:
            print('x_probability values = ', probability_values[k1].evalf(subs={t: t_value, d: d_value}))
            # print('x_probability t, d +0.1 ', probability_values[k1].evalf(subs={t: t_value, d: d_value + 0.1}))
            # print('x_probability t, d +0.2 ', probability_values[k1].evalf(subs={t: t_value, d: d_value + 0.2}))
            # print('x_probability t, d +0.3 ', probability_values[k1].evalf(subs={t: t_value, d: d_value + 0.3}))
            # print('x_probability t, d +0.4 ', probability_values[k1].evalf(subs={t: t_value, d: d_value + 0.4}))
            # print('x_probability t, d +0.5 ', probability_values[k1].evalf(subs={t: t_value, d: d_value + 0.5}))
            # print('x_probability t + 0.1, d ', probability_values[k1].evalf(subs={t: t_value + 0.1, d: d_value}))
            # print('x_probability t + 0.2, d ', probability_values[k1].evalf(subs={t: t_value + 0.2, d: d_value}))
            # print('x_probability t + 0.3, d ', probability_values[k1].evalf(subs={t: t_value + 0.3, d: d_value}))
            # print('x_probability t + 0.4, d ', probability_values[k1].evalf(subs={t: t_value + 0.4, d: d_value}))
            # print('x_probability t + 0.5, d ', probability_values[k1].evalf(subs={t: t_value + 0.5, d: d_value}))
            # print('x_probability t + 1, d + 1', probability_values[k1].evalf(subs={t: t_value + 1, d: d_value + 1}))
        Label(mul_root, text="X(" + str(k1+1) + ") ").grid(row=k1_value + k1 + 5, column=0)
        Label(mul_root, text=str(probability_values[k1])).grid(row=k1_value + k1 + 5, column=1)
        # Label(mul_root, text=str(y_probability[k1])).grid(row=k1_value + k1 + 5, column=2)


    # for k1 in range(0, len(probability_values)):
    #     print('x_probability t, d +0.1 ', probability_values[k1].evalf(subs={t: t_value, d: d_value + 0.1}))


    with open("Output.txt", "a") as text_file:
        print(' ----------------------------------', file=text_file)
        # print(' y_parametric array = ', y_parametric_array, file=text_file)
        # print(' x_parametric array = ', x_parametric_array, file=text_file)
        # print(' z_parametric_array array = ', z_parametric_array, file=text_file)
        print(' ----------------------------------', file=text_file)
        print(' parametric Game value = ' + str(game_value), file=text_file)
        # print(' X probabilities = ' + str(x_probability), file=text_file)
        for i in range(len(probability_values)):
            print("X" + str(i+1) + " ( d,t ) = {}".format(str(probability_values[i])), file=text_file)
        # print(' Y probabilities = ' + str(y_probability), file=text_file)

    mul_root.mainloop()
