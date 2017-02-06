# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from tkinter import *
from simplex_parametric_right import *
from graph_gui import *


def report_window(root, matrix, vector, k_value):
    report_root = Toplevel(root)
    report_root.title("game model report")
    report_root.geometry("1200x800")
    approx_centers = [0.0, 0.5, 1.5, 7.0]
    # top level bar
    Label(report_root, text=' K ').grid(row=0, column=0)
    Label(report_root, text=' t = ' + str(approx_centers[0]) + ' ').grid(row=0, column=1, sticky="nsew")
    Label(report_root, text=' t = ' + str(approx_centers[1]) + ' ').grid(row=0, column=2, sticky="nsew")
    Label(report_root, text=' t = ' + str(approx_centers[2]) + ' ').grid(row=0, column=3, sticky="nsew")
    Label(report_root, text=' t = ' + str(approx_centers[3]) + ' ').grid(row=0, column=4, sticky="nsew")

    # left side bar
    for k in range(k_value + 1):
        value = " V( " + str(k) + " ) "
        Label(report_root, text=value).grid(row=k + 1, column=0)

    Label(report_root, text=' V( t ) ').grid(row=k + 1, column=0)
    Label(report_root, text=' R1( t ) ').grid(row=k + 2, column=0)
    Label(report_root, text=' R2( t ) ').grid(row=k + 3, column=0)
    Label(report_root, text=' R3( t ) ').grid(row=k + 4, column=0)

    v = 0
    length = len(approx_centers)
    for app in range(length):
        parametric_array = [0 for x in range(len(vector))]
        x_b_image_matrix = parametric_simplex_solution(matrix, vector, k_value, approx_centers[app], parametric_array)

        for k in range(0, k_value + 1):
            s_item = 0
            for j in range(0, len(vector)):
                s_item += x_b_image_matrix[k][j]
            Label(report_root, text=str(s_item)).grid(row=k + 1, column=app + 1)

        v = 1/sum(parametric_array)
        Label(report_root, text=str(v)).grid(row=k + 1, column=app + 1)
        Label(report_root, text=str(parametric_array[0])).grid(row=k + 2, column=app + 1)
        Label(report_root, text=str(parametric_array[1])).grid(row=k + 3, column=app + 1)
        Label(report_root, text=str(parametric_array[2])).grid(row=k + 4, column=app + 1)

        def create_graph_window():
            graph_window(report_root, v)

        Button(report_root, text='draw V(t) graph', command=create_graph_window).grid(row=k + 5, column=app + 1, padx=10, pady=10)

    report_root.mainloop()



