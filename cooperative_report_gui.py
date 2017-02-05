# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from tkinter import *
from cooperative import *


def graph_c_window(root, matrix, t_value):
    graph_c_root = Toplevel(root)
    graph_c_root.title("cooperative game report")
    graph_c_root.geometry("600x600")

    # enter matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            Label(graph_c_root, text=str(matrix[i][j])).grid(row=i + 1, column=j + 1, padx=10, pady=10)

    Label(graph_c_root, text='numerical values of cooperation matrix in  t = ' + str(t_value) + '').grid(row=i + 2, column= 1, padx=10, pady=10)

    value_matrix = set_value_to_matrix(matrix, t_value)

    for i in range(len(value_matrix)):
        for j in range(len(value_matrix)):
            Label(graph_c_root, text=str(value_matrix[i][j])).grid(row=i + 2 + len(matrix), column=j + 1, padx=10, pady=10)

    graph_c_root.mainloop()
