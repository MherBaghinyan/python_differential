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
    print(' parametric F max = ', function_max_parametric)
    game_value = 1/function_max_parametric
    print(' parametric Game value = ', game_value)
    print(' parametric Game value = ', game_value.evalf(subs={t: t_value, d: d_value}))
    # print(' parametric Game value = good 0.5', game_value.evalf(subs={t: t_value, d: 0.5}))

    x_probability = [x * game_value for x in x_parametric_array]
    y_probability = [x * game_value for x in y_parametric_array]

    # for j in range(0, len(x_probability)):
    #     if x_probability[j] > 1:
    #         x_probability[j] = 0
    #         x_parametric_array[j] = 0
    #     if y_probability[j] > 1:
    #         y_probability[j] = 0
    #         y_parametric_array[j] = 0

    print(' x_parametric array = ', x_parametric_array)
    # print(' y_parametric array = ', y_parametric_array)
    print(' z_parametric_array array = ', z_parametric_array)
    # print(' y_probability array = ', y_probability)
    print(' x_probability array = ', x_probability)

    # res = multy_nonlinear_optimality(z_parametric_array, d_value, t_value)
    # print("optimality = ", res)

    # Label(mul_root, text=" - ").grid(row=k1_value + 1, column=1)
    Label(mul_root, text=" Game Value = " + str(game_value)).grid(row=k1_value + 2, column=1)
    Label(mul_root, text=" - ").grid(row=k1_value + 3, column=1)
    Label(mul_root, text=" X probabilities  ").grid(row=k1_value + 4, column=0)
    # Label(mul_root, text=" Y probabilities ").grid(row=k1_value + 4, column=2)
    sum = 0
    for k1 in range(0, len(x_probability)):
        # print('y_probability values ', y_probability[k1].evalf(subs={t: t_value, d: d_value}))
        print('x_probability values = ', x_probability[k1].evalf(subs={t: t_value, d: d_value}))
        sum += x_probability[k1].evalf(subs={t: t_value, d: d_value})
        Label(mul_root, text="X(" + str(basis_vector[k1]) + ") ").grid(row=k1_value + k1 + 5, column=0)
        Label(mul_root, text=str(x_probability[k1])).grid(row=k1_value + k1 + 5, column=1)
        # Label(mul_root, text=str(y_probability[k1])).grid(row=k1_value + k1 + 5, column=2)
    print("sum = ", sum)

    # for k1 in range(0, len(x_probability)):
    #     print('x_probability 0.5 = ', x_probability[k1].evalf(subs={t: t_value, d: 0.5}))

    with open("Output.txt", "a") as text_file:
        print(' ----------------------------------', file=text_file)
        # print(' y_parametric array = ', y_parametric_array, file=text_file)
        # print(' x_parametric array = ', x_parametric_array, file=text_file)
        # print(' z_parametric_array array = ', z_parametric_array, file=text_file)
        print(' ----------------------------------', file=text_file)
        print(' parametric Game value = ' + str(game_value), file=text_file)
        print(' X probabilities = ' + str(x_probability), file=text_file)
        # print(' Y probabilities = ' + str(y_probability), file=text_file)

    mul_root.mainloop()
