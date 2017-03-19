# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
# http://www.java2s.com/Code/Python/GUI-Tk/LabelborderRAISEDSUNKENFLATRIDGEGROOVESOLID.htm
from project_files.cooperative import *
from project_files.services.graph_gui import *


def graph_c_window(root, matrix, t_value):
    graph_c_root = Toplevel(root)
    graph_c_root.title("cooperative game report")
    graph_c_root.geometry("1000x400")

    xf = Frame(graph_c_root, relief=GROOVE, borderwidth=2)
    Label(graph_c_root, text='parametric values of cooperation matrix ').place(relx=0.1, rely=0.10, anchor=NW)
    xf.place(relx=0.1, rely=0.145, anchor=NW)

    f_vec = [0 for x in range(len(matrix) * len(matrix[0]))]

    f_indx = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            f_vec[f_indx] = matrix[i][j]
            f_indx += 1

    def create_graph_window(f_index):
        graph_window(graph_c_root, f_vec[f_index], 0, 1.1)

    # enter matrix
    f_index = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            Label(xf, text=str(f_vec[f_index]), relief=GROOVE).grid(row=f_index + 1, column=1, padx=10, pady=10)
            Label(xf, text='i= ' + str(i) + ' j= ' + str(j), relief=GROOVE).grid(row=f_index + 1, column=0, padx=10, pady=10)
            Button(xf, text='draw item graph', command= lambda f_index=f_index: create_graph_window(f_index)).grid(row=1 + f_index, column=2, padx=10, pady=10)
            f_index += 1

    # pf = Frame(graph_c_root, relief=GROOVE, borderwidth=2)
    # pf.place(relx=0.1, rely=0.4, anchor=NW)
    #
    # Label(graph_c_root, text='graphical representation of matrix functions').place(relx=0.1, rely=0.37, anchor=NW)
    #
    # def create_graph_window(i, j):
    #     print(matrix[i][j])
    #     graph_window(graph_c_root, matrix[i][j], 0, 1.1)
    #
    # step = len(matrix) + 7
    # for i in range(len(matrix)):
    #     for j in range(len(matrix)):
    #         Button(pf, text='draw item graph', command= lambda i=i, j=j: create_graph_window(i, j)).grid(row=step + i, column=j + 1, padx=10, pady=10)

    graph_c_root.mainloop()
