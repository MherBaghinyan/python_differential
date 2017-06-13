# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from tkinter import *

from sympy.parsing.sympy_parser import parse_expr

from project_files.multy_parametric.multiparametric_result_gui import *


def multi_window(root, n_value, m_value):
    multi_root = Toplevel(root)
    multi_root.title("Multi Parametric game model solver")
    multi_root.geometry("1200x600")

    Label(multi_root, text='N = ').grid(row=0, column=0)
    Label(multi_root, text=n_value).grid(row=0, column=1)
    Label(multi_root, text='M = ').grid(row=1, column=0)
    Label(multi_root, text=m_value).grid(row=1, column=1)

    Label(multi_root, text='K1 = ').grid(row=0, column=2)
    k1 = Entry(multi_root, relief=RIDGE)
    k1.grid(row=0, column=3, sticky=NSEW, padx=5, pady=5)
    k1.insert(END, 2)

    Label(multi_root, text='K2 = ').grid(row=1, column=2)
    k2 = Entry(multi_root, relief=RIDGE)
    k2.grid(row=1, column=3, sticky=NSEW, padx=5, pady=5)
    k2.insert(END, 2)

    Label(multi_root, text='approximation center d=').grid(row=2, column=2)
    d = Entry(multi_root, relief=RIDGE)
    d.grid(row=2, column=3, sticky=NSEW, padx=5, pady=5)
    d.insert(END, 10)

    Label(multi_root, text='approximation center t=').grid(row=3, column=2)
    t = Entry(multi_root, relief=RIDGE)
    t.grid(row=3, column=3, sticky=NSEW, padx=5, pady=5)
    t.insert(END, 10)

    Label(multi_root, text='Enter parametric ').grid(row=4, column=0)
    Label(multi_root, text='game model below').grid(row=4, column=1)

    rows = []
    for i in range(n_value):
        cols = []
        for j in range(m_value):
            e = Entry(multi_root, relief=RIDGE)
            e.grid(row=i + 5, column=j, sticky=NSEW, padx=5, pady=5)
            e.insert(END, R_matrix[i][j])
            cols.append(e)
        rows.append(cols)

    v_recovered = StringVar()
    z_matrix = [[0] * len(rows) for x in range(len(rows))]

    strategies_recovered = [0 for x in range(len(z_matrix))]
    parametric_array = [0 for x in range(len(z_matrix))]

    def on_press():
        i = 0
        for row in rows:
            j = 0
            for col in row:
                z_matrix[i][j] = parse_expr(col.get())
                j += 1
                print(col.get())
            i += 1
            print()

        recover_value = 0
        k1_value = parse_expr(k1.get())
        k2_value = parse_expr(k2.get())
        d_value = parse_expr(d.get())
        t_value = parse_expr(t.get())
        multy_window(multi_root, z_matrix, k1_value, k2_value, d_value, t_value)

    Button(multi_root, text='Solve', command=on_press).grid()
    multi_root.mainloop()
