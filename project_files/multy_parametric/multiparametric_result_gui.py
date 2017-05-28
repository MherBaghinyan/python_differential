# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from project_files.multy_parametric.multiparametric import *
from project_files.services.graph_gui import *
from project_files.services.optimization_util import *


def multy_window(root, s_matrix, k1_value, k2_value, d_value, t_value):
    mul_root = Toplevel(root)
    mul_root.title("game model solution")
    mul_root.geometry("800x400")

    # top level bar
    # Label(mul_root, text=' K ').grid(row=0, column=0)

    k1_value = 3
    k2_value = 3
    d_value = 1
    t_value = 1

# x1 = [179.95 ,  156.12 , 90 ,  1.0,  0.0,  0.0]
# x2 = [89.95 , 179.87 , 155 ,   0.0,  1.0,  0.0]
# x3 = [180,  156 , 177 ,  0.0,  0.0,  1.0]

    s_matrix = [[179.95 + sin(t), 156.12 + 1/(t**2), 90 + d**3, d*(1-0.2*t) + 1],
                [89.95 + 2*t / ((d + 1) ** 3) ** -0.5, 179.87 + 90*t/2 + d, acos(1/t), exp(t + d)],
                [180 + 4/(d+t), 156 + 5 + d, 155 + 155*t, sqrt(d**2 + t) + 4],
                [77 + t**3, 90.4 + acos(t) + atan(d), 177 + (d**3)/cos(2 * t), tanh(4*exp(d))]]

    solution_matrix = initiate_simplex_matrix(s_matrix, [], [], [], k1_value, k2_value, d_value, t_value)

    rows = len(s_matrix)

    x_parametric_array = [0 for x in range(rows)]
    y_parametric_array = [0 for x in range(rows)]

    z_parametric_array = [0 for x in range(rows*2)]

    function_max_parametric = 0
    for k1 in range(0, k1_value + 1):
        for k2 in range(0, k2_value + 1):
            current_image_table = solution_matrix[k1][k2]
            table_len = len(current_image_table[0])
            for i in range(rows):
                indice = int((table_len - 1) / 2) + 1
                y_parametric_array[i] += current_image_table[0][indice + i]*((t-t_value)**k1)*((d-d_value)**k2)
                item = current_image_table[i][0]
                if item > 0 and i > 0:
                    x_parametric_array[i - 1] += item*((t-t_value)**k1)*((d-d_value)**k2)

            for j in range(1, table_len):
                z_parametric_array[j - 1] += current_image_table[0][j]*((t-t_value)**k1)*((d-d_value)**k2)

            f_image = current_image_table[0][0]
            function_max_parametric += f_image*((t-t_value)**k1)*((d-d_value)**k2)

    print(' parametric F max = ', function_max_parametric)
    game_value = 1/function_max_parametric
    print(' parametric Game value = ', game_value)

    x_probability = [x * game_value for x in x_parametric_array]
    y_probability = [x * game_value for x in y_parametric_array]

    for j in range(0, len(x_probability)):
        if x_probability[j] > 1:
            x_probability[j] = 0
            x_parametric_array[j] = 0
        if y_probability[j] > 1:
            y_probability[j] = 0
            y_parametric_array[j] = 0

    print(' y_parametric array = ', y_parametric_array)
    print(' x_parametric array = ', x_parametric_array)
    print(' z_parametric_array array = ', z_parametric_array)
    print('x_probability array = ', x_probability)
    print('y_probability array = ', y_probability)

    res = multy_nonlinear_optimality(z_parametric_array, d_value, t_value)
    print("optimality = ", res)

    Label(mul_root, text=" - ").grid(row=k1_value + 1, column=1)
    Label(mul_root, text=" Game Value = " + str(game_value)).grid(row=k1_value + 2, column=2)
    Label(mul_root, text=" - ").grid(row=k1_value + 3, column=1)
    Label(mul_root, text=" X probabilities  ").grid(row=k1_value + 4, column=1)
    Label(mul_root, text=" Y probabilities ").grid(row=k1_value + 4, column=2)
    for k1 in range(0, len(x_probability)):
        Label(mul_root, text=str(x_probability[k1])).grid(row=k1_value + k1 + 5, column=1)
        Label(mul_root, text=str(y_probability[k1])).grid(row=k1_value + k1 + 5, column=2)

    with open("Output.txt", "a") as text_file:
        print(' ----------------------------------', file=text_file)
        print(' x_parametric array  = ', x_parametric_array, file=text_file)
        print(' y_parametric array = ', y_parametric_array, file=text_file)
        print(' z_parametric_array array = ', z_parametric_array, file=text_file)
        print(' ----------------------------------', file=text_file)
        print(' parametric Game value = ' + str(game_value), file=text_file)
        print(' X probabilities = ' + str(x_probability), file=text_file)
        print(' Y probabilities = ' + str(y_probability), file=text_file)

    mul_root.mainloop()
