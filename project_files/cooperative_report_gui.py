# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
# http://www.java2s.com/Code/Python/GUI-Tk/LabelborderRAISEDSUNKENFLATRIDGEGROOVESOLID.htm
from project_files.cooperative import *
from project_files.services.graph_gui import *


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

    Label(graph_c_root, text='graphical representation of matrix functions').place(relx=0.1, rely=0.40, anchor=NW)

    def create_graph_window():
        graph_window(graph_c_root, matrix[0][0], 0, 1)

    step = i + 3
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            Button(graph_c_root, text='draw item graph', command=create_graph_window).grid(row=step + i, column=j, padx=10, pady=10)

    graph_c_root.mainloop()
