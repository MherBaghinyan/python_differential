# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from project_files.multy_parametric.multiparametric import *
from project_files.one_parameter.graph_gui import *
from project_files.services.optimization_util import *


def multy_window(root, s_matrix, k1_value, k2_value, d_value, t_value):
    mul_root = Toplevel(root)
    mul_root.title("game model solution")
    mul_root.geometry("1200x800")

    # top level bar
    # Label(mul_root, text=' K ').grid(row=0, column=0)
    solution_matrix = initiate_simplex_matrix(R_matrix, [], [], [], k1_value, k2_value, d_value, t_value)

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

    print(' y_parametric array = ', y_parametric_array)
    print(' x_parametric array = ', x_parametric_array)
    print(' z_parametric_array array = ', z_parametric_array)

    x_probability = [x * game_value for x in x_parametric_array]
    y_probability = [x * game_value for x in y_parametric_array]
    print('x_probability array = ', x_probability)
    print('y_probability array = ', y_probability)

    res = multy_nonlinear_optimality(z_parametric_array, d_value, t_value)
    print("optimality = ", res)

    Label(mul_root, text=" Game Value = "+ str(game_value)).grid(row=k1_value + 2, column=1)
    Label(mul_root, text=" X probabilities = " + str(x_probability)).grid(row=k1_value + 3, column=1)
    Label(mul_root, text=" Y probabilities = " + str(y_probability)).grid(row=k1_value + 4, column=1)

    # for i in range(len(x_probability)):
    #     label_indice = " X probabilities"

    mul_root.mainloop()
