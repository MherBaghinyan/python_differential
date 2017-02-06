# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from tkinter import *
from simplex_parametric_right import *
from graph_gui import *


def one_window(root, matrix, vector, k_value, t_value):
    one_root = Toplevel(root)
    one_root.title("game model report")
    one_root.geometry("1200x800")
    approx_centers = [0.0, 0.5, 1.5, 7.0]
    # top level bar
    Label(one_root, text=' K ').grid(row=0, column=0)
    # Label(one_root, text=' t = ' + str(approx_centers[0]) + ' ').grid(row=0, column=1, sticky="nsew")
    # Label(one_root, text=' t = ' + str(approx_centers[1]) + ' ').grid(row=0, column=2, sticky="nsew")
    # Label(one_root, text=' t = ' + str(approx_centers[2]) + ' ').grid(row=0, column=3, sticky="nsew")
    # Label(one_root, text=' t = ' + str(approx_centers[3]) + ' ').grid(row=0, column=4, sticky="nsew")

    # left side bar
    for k in range(k_value + 1):
        value = " V( " + str(k) + " ) "
        Label(one_root, text=value).grid(row=k + 1, column=0)

    Label(one_root, text=' V( t ) ').grid(row=k + 2, column=0)
    Label(one_root, text=' R1( t ) ').grid(row=k + 3, column=0)
    Label(one_root, text=' R2( t ) ').grid(row=k + 4, column=0)
    Label(one_root, text=' R3( t ) ').grid(row=k + 5, column=0)

    v = 0

    parametric_array = [0 for x in range(len(vector))]
    x_b_image_matrix = parametric_simplex_solution(matrix, vector, k_value, t_value, parametric_array)

    for k in range(0, k_value + 1):
        s_item = 0
        for j in range(0, len(vector)):
            s_item += x_b_image_matrix[k][j]
        Label(one_root, text=str(s_item)).grid(row=k + 1, column=0 + 1)

    v = 1/sum(parametric_array)
    Label(one_root, text=str(v)).grid(row=k + 2, column=0 + 1)
    Label(one_root, text=str(parametric_array[0])).grid(row=k + 3, column=0 + 1)
    Label(one_root, text=str(parametric_array[1])).grid(row=k + 4, column=0 + 1)
    Label(one_root, text=str(parametric_array[2])).grid(row=k + 5, column=0 + 1)

    def create_graph_window():
        graph_window(one_root, v)

    Button(one_root, text='draw V(t) graph', command=create_graph_window).grid(row=k + 6, column=0 + 1, padx=10, pady=10)

    one_root.mainloop()



