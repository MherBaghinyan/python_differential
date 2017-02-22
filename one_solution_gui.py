# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from tkinter import *
from simplex_parametric_right import *
from graph_gui import *


def one_window(root, matrix, vector, z_array, k_value, t_value):
    one_root = Toplevel(root)
    one_root.title("game model solution")
    one_root.geometry("1200x800")

    # top level bar
    Label(one_root, text=' K ').grid(row=0, column=0)
    Label(one_root, text=' V( t ) ').grid(row=k_value + 2, column=0)
    solution_matrix = parametric_simplex_solution(matrix, vector, z_array, k_value, t_value)

    step = 0

    for s in range(len(solution_matrix)):
        each_step = solution_matrix[s]
        parameter_start = each_step[0]
        parameter_end = each_step[1]
        image_matrixes = each_step[2]
        basis_vector = each_step[3]

        for k in range(0, k_value + 1):

            value = " V( " + str(k) + " ) "
            Label(one_root, text=value).grid(row=k + 1, column=0)

            image_matrix = image_matrixes[k]
            printTableu(image_matrix)
            rows = len(image_matrix)
            s_item = 0
            for i in range(1, rows):
                s_item += image_matrix[i][0]
            Label(one_root, text=str(s_item)).grid(row=step + k + 1, column=0 + 1)

        parametric_array = get_parametric_array(image_matrixes, len(vector), k, t_value, basis_vector)

        for b in range(len(basis_vector)):
            if basis_vector[b] > len(basis_vector):
                parametric_array[b] = 0
                basis_vector[b] = 1

        v = 0
        for i in range(len(basis_vector)):
            label_indice = " X" + str(basis_vector[i]) + " ( t ) "
            Label(one_root, text=label_indice).grid(row=k_value + 3 + i, column=0)
            v += parametric_array[i]*z_array[basis_vector[i] - 1]

        v = 1 / v
        Label(one_root, text=str(v)).grid(row=step + k + 2, column=0 + 1)
        for i in range(len(parametric_array)):
            Label(one_root, text=str(parametric_array[i] * v)).grid(row=step + k + 3 + i, column=0 + 1)

        with open("Output.txt", "a") as text_file:
            print("----------------------", file=text_file)
            print("F max = {}".format(str(v)), file=text_file)
            for i in range(len(parametric_array)):
                print("X1 = {}".format(str(parametric_array[i] * v)), file=text_file)

        parametric_array = [0 for x in range(len(vector))]

        def create_graph_window():
            graph_window(one_root, v, parameter_start, parameter_end)

        Button(one_root, text='draw V(t) graph', command=create_graph_window).grid(row=step + k + 6, column=0 + 1, padx=10, pady=10)
        step = k + 7

    one_root.mainloop()



