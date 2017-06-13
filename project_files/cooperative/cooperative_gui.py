# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from sympy.parsing.sympy_parser import parse_expr

from project_files.cooperative.cooperative_report_gui import *
from project_files.cooperative.cooperative_dirichle_gui import *
from project_files.cooperative.cooperative_first_gui import *
from project_files.cooperative.cooperative import *


def cooperative_window(root, n_value, m_value):
    cooperative_root = Toplevel(root)
    cooperative_root.title("Cooperative game model solver")
    cooperative_root.geometry("800x400")

    Label(cooperative_root, text='N = ').grid(row=0, column=0)
    Label(cooperative_root, text=n_value).grid(row=0, column=1)
    Label(cooperative_root, text='M = ').grid(row=1, column=0)
    Label(cooperative_root, text=m_value).grid(row=1, column=1)

    Label(cooperative_root, text='K = ').grid(row=0, column=2)
    k1 = Entry(cooperative_root, relief=RIDGE)
    k1.grid(row=0, column=3, sticky=NSEW, padx=5, pady=5)
    k1.insert(END, 3)

    # Label(cooperative_root, text='approximation center t=').grid(row=1, column=2)
    # t1 = Entry(cooperative_root, relief=RIDGE)
    # t1.grid(row=1, column=3, sticky=NSEW, padx=5, pady=5)
    # t1.insert(END, 1.55)

    Label(cooperative_root, text='Sympathy parameter = ').grid(row=4, column=2)
    s1 = Entry(cooperative_root, relief=RIDGE)
    s1.grid(row=4, column=3, sticky=NSEW, padx=5, pady=5)
    s1.insert(END, 0.8)

    Label(cooperative_root, text='Enter first player game matrix').grid(row=5, column=0)

    a_ = [[40, 10], [50, 15]]
    # enter matrix
    rows_a = []
    for i in range(n_value):
        cols = []
        for j in range(m_value):
            e = Entry(cooperative_root, relief=RIDGE)
            e.grid(row=i + 6, column=j, sticky=NSEW, padx=5, pady=5)
            e.insert(END, a_[i][j])
            cols.append(e)
        rows_a.append(cols)

    a_matrix = [[0] * len(rows_a) for x in range(len(rows_a))]

    next_matrix_i = i + 7
    Label(cooperative_root, text=' Enter second player game matrix').grid(row=next_matrix_i, column=0)

    b_ = [[40, 50], [10, 15]]
    # enter matrix
    rows_b = []
    for i in range(n_value):
        cols = []
        for j in range(m_value):
            e = Entry(cooperative_root, relief=RIDGE)
            e.grid(row=i + next_matrix_i + 1, column=j, sticky=NSEW, padx=5, pady=5)
            e.insert(END, b_[i][j])
            cols.append(e)
        rows_b.append(cols)

    b_matrix = [[0] * len(rows_b) for x in range(len(rows_b))]

    p_recovered = [StringVar() for x in range(m_value)]
    i = 0
    for i in range(m_value):
        Label(cooperative_root, textvariable=p_recovered[i]).grid(row=10 + i, column=1)

    p_values = [StringVar() for x in range(m_value)]
    for j in range(m_value):
        Label(cooperative_root, textvariable=p_values[j]).grid(row=10 + i + j, column=1)

    def on_press_2():
        i = 0
        for row in rows_a:
            j = 0
            for col in row:
                a_matrix[i][j] = parse_expr(col.get())
                j += 1
            i += 1
            print()

        i = 0
        for row in rows_b:
            j = 0
            for col in row:
                b_matrix[i][j] = parse_expr(col.get())
                j += 1
            i += 1
            print()

            # iterations = parse_expr(i_entry.get())
            k = parse_expr(k1.get())
            # t_value = parse_expr(t1.get())
            sympathy = parse_expr(s1.get())

        result = cooperative_matrix(a_matrix, b_matrix, 1, k, sympathy)

        graph_c_window(cooperative_root, result, sympathy)

    def on_press_1():
        i = 0
        for row in rows_a:
            j = 0
            for col in row:
                a_matrix[i][j] = parse_expr(col.get())
                j += 1
            i += 1
            print()

        i = 0
        for row in rows_b:
            j = 0
            for col in row:
                b_matrix[i][j] = parse_expr(col.get())
                j += 1
            i += 1
            print()

            # iterations = parse_expr(i_entry.get())
            k = parse_expr(k1.get())
            # t_value = parse_expr(t1.get())
            sympathy = parse_expr(s1.get())

        result = cooperative_matrix_1(a_matrix, b_matrix, k, sympathy)

        graph_c1_window(cooperative_root, result, sympathy)

    def on_press_dir():
        i = 0
        for row in rows_a:
            j = 0
            for col in row:
                a_matrix[i][j] = parse_expr(col.get())
                j += 1
            i += 1
            print()

        i = 0
        for row in rows_b:
            j = 0
            for col in row:
                b_matrix[i][j] = parse_expr(col.get())
                j += 1
            i += 1
            print()

            # iterations = parse_expr(i_entry.get())
            k = parse_expr(k1.get())
            # t_value = parse_expr(t1.get())
            sympathy = parse_expr(s1.get())

        result = cooperative_matrix_dirichle(a_matrix, b_matrix, k, sympathy)

        graph_cd_window(cooperative_root, result, sympathy)

    Button(cooperative_root, text='Solve Exponential-Dirichlet', command=on_press_dir).grid(row=20, column=4, padx=5, pady=5)
    Button(cooperative_root, text='Solve Exponential 1', command=on_press_1).grid(row=21, column=4, padx=5, pady=5)
    Button(cooperative_root, text='Solve Exponential 2', command=on_press_2).grid(row=22, column=4, padx=5, pady=5)
    cooperative_root.mainloop()
