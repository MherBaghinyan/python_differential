# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from project_files.one_parameter.simplex_parametric_right import *
from project_files.services.graph_gui import *


def one_window(root, matrix, vector, z_array, k_value, t_value, bound_):
    one_root = Toplevel(root)
    one_root.title("game model solution")
    one_root.geometry("1200x700")

    step = 0

    # top level bar
    #Label(one_root, text=' K ').grid(row=0, column=0)
    solution_matrix = parametric_simplex_solution(matrix, vector, z_array, k_value, t_value, bound_)

    parameter_start = parametric_array = [0 for x in range(len(solution_matrix))]
    parameter_end = parametric_array = [0 for x in range(len(solution_matrix))]

    for s in range(len(solution_matrix)):
        each_step = solution_matrix[s]
        parameter_start[s] = each_step[0]
        parameter_end[s] = each_step[1]
        image_matrixes = each_step[2]
        basis_vector = each_step[3]
        t_value = each_step[4]
        for k in range(0, k_value + 1):

            value = " V( " + str(k) + " ) "
            #Label(one_root, text=value).grid(row=k + 1, column=0)

            image_matrix = image_matrixes[k]
            printTableu(image_matrix)
            rows = len(image_matrix)
            s_item = 0
            for i in range(1, rows):
                s_item += image_matrix[i][0]
            #Label(one_root, text=str(s_item)).grid(row=step + k + 1, column=0 + 1)

        parametric_array = get_parametric_array(image_matrixes, len(vector), k, t_value, basis_vector)

        for b in range(len(basis_vector)):
            if basis_vector[b] > len(basis_vector):
                parametric_array[b] = 0
                basis_vector[b] = 1

        game_value = 1/sum(parametric_array)

        print(parametric_array)
        print(game_value)

        v = 0
        Label(one_root, text=' V( t ) ').grid(row=step + k_value + 2, column=0)

        for i in range(len(basis_vector)):
            label_indice = " X" + str(basis_vector[i]) + " ( t ) "
            Label(one_root, text=label_indice).grid(row=step + k_value + 3 + i, column=0)
            v += parametric_array[i]*z_array[basis_vector[i] - 1]

        v = 1 / v
        Label(one_root, text=str(v)).grid(row=step + k + 2, column=0 + 1)
        for i in range(len(parametric_array)):
            Label(one_root, text=str(parametric_array[i] * v)).grid(row=step + k + 3 + i, column=0 + 1)

        with open("Output.txt", "a") as text_file:
            print("----------------------", file=text_file)
            print("V max = {}".format(str(v)), file=text_file)
            for i in range(len(parametric_array)):
                print("X" + str(basis_vector[i]) + " ( t ) = {}".format(str(parametric_array[i] * v)), file=text_file)

        parametric_array = [0 for x in range(len(vector))]

        def create_graph_window(s):
            graph_window(one_root, v, parameter_start[s], parameter_end[s])

        Label(one_root, text= str(parameter_start[s]) + " <= t < = " + str(parameter_end[s])).grid(row=step + k + 6, column=0 + 1)
        Button(one_root, text='draw V(t) graph', command=lambda s=s: create_graph_window(s)).grid(row=step + k + 7, column=0 + 1, padx=10, pady=10)
        step += k + 7

    one_root.mainloop()



