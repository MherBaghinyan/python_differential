# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
# http://www.java2s.com/Code/Python/GUI-Tk/LabelborderRAISEDSUNKENFLATRIDGEGROOVESOLID.htm
from project_files.cooperative.cooperative_first import *
from project_files.services.graph_gui import *


def graph_c1_window(root, matrix, t_value):
    graph_c1_root = Toplevel(root)
    graph_c1_root.title("cooperative game report")
    graph_c1_root.geometry("1000x400")

    xf = Frame(graph_c1_root, relief=GROOVE, borderwidth=2)
    Label(graph_c1_root, text='parametric values of cooperation matrix ').place(relx=0.1, rely=0.10, anchor=NW)
    xf.place(relx=0.1, rely=0.145, anchor=NW)

    f_vec = [0 for x in range(len(matrix) * len(matrix[0]))]

    f_indx = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            f_vec[f_indx] = matrix[i][j]
            f_indx += 1

    def create_graph_window(f_index):
        graph_window(graph_c1_root, f_vec[f_index], 0, 1.1)

    # enter matrix
    f_index = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            Label(xf, text=str(f_vec[f_index]), relief=GROOVE).grid(row=f_index + 1, column=1, padx=10, pady=10)
            Label(xf, text='i= ' + str(i) + ' j= ' + str(j), relief=GROOVE).grid(row=f_index + 1, column=0, padx=10, pady=10)
            Button(xf, text='draw item graph', command= lambda f_index=f_index: create_graph_window(f_index)).grid(row=1 + f_index, column=2, padx=10, pady=10)
            f_index += 1

    with open("Output.txt", "a") as text_file:
        print(" ----------------------", file=text_file)
        for i in range(len(f_vec)):
            print(str(f_vec[i]), file=text_file)

    graph_c1_root.mainloop()
