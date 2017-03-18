# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
# http://www.java2s.com/Code/Python/GUI-Tk/LabelborderRAISEDSUNKENFLATRIDGEGROOVESOLID.htm
from tkinter import *

from project_files.cooperative import *


def graph_c_window(root, matrix, t_value):
    graph_c_root = Toplevel(root)
    graph_c_root.title("cooperative game report")
    graph_c_root.geometry("800x400")

    xf = Frame(graph_c_root, relief=GROOVE, borderwidth=2)
    Label(graph_c_root, text='parametric values of cooperation matrix ').place(relx=0.1, rely=0.10, anchor=NW)
    xf.place(relx=0.1, rely=0.145, anchor=NW)


    # enter matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            Label(xf, text=str(matrix[i][j]), relief=GROOVE).grid(row=i + 1, column=j + 1, padx=10, pady=10)

    pf = Frame(graph_c_root, relief=GROOVE, borderwidth=2)
    pf.place(relx=0.1, rely=0.325, anchor=NW)

    Label(graph_c_root, text='numerical values of cooperation matrix for approximation = ' + str(t_value) + '').place(relx=0.1, rely=0.29, anchor=NW)

    value_matrix = set_value_to_matrix(matrix, t_value)

    for i in range(len(value_matrix)):
        for j in range(len(value_matrix)):
            Label(pf, text=str(value_matrix[i][j]), relief=RAISED, anchor=W).grid(row=i + 2 + len(matrix), column=j + 1, padx=10, pady=10)

    graph_c_root.mainloop()
