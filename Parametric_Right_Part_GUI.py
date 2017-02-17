# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
# http://docs.sympy.org/dev/modules/parsing.html
from multiparametric import *
from simplex_parametric_right import *
from tkinter import *
from sympy.parsing.sympy_parser import parse_expr
from extended_report_gui import *
from one_solution_gui import *


def parametric_window(root, n_value, m_value):
    parametric_root = Toplevel(root)
    parametric_root.title("Parametric game model solver")
    parametric_root.geometry("1200x600")

    k = 2
    t_value = 0

    Label(parametric_root, text='N = ').grid(row=0, column=0)
    Label(parametric_root, text=n_value).grid(row=0, column=1)
    Label(parametric_root, text='M = ').grid(row=1, column=0)
    Label(parametric_root, text=m_value).grid(row=1, column=1)

    Label(parametric_root, text='K = ').grid(row=0, column=2)
    k1 = Entry(parametric_root, relief=RIDGE)
    k1.grid(row=0, column=3, sticky=NSEW, padx=5, pady=5)
    k1.insert(END, k)

    Label(parametric_root, text='Parameter to work with = t').grid(row=0, column=9)

    Label(parametric_root, text='approximation center t =').grid(row=3, column=2)
    t1 = Entry(parametric_root, relief=RIDGE)
    t1.grid(row=3, column=3, sticky=NSEW, padx=5, pady=5)
    t1.insert(END, t_value)

    # x_1 = [[179.95, 156.12, 90],
    #       [89.95, 179.87, 155],
    #       [180, 156, 177]]

    x_1 = [
        [1.0, 2.0, 1.0],
        [3.0, 0.0, 2.0],
        [1.0, 4.0, 0.0]
    ]

    # enter matrix
    rows = []
    for i in range(n_value):
        cols = []
        for j in range(m_value):
            e = Entry(parametric_root, relief=RIDGE)
            e.grid(row=i + 4, column=j, sticky=NSEW, padx=5, pady=5)
            e.insert(END, x_1[i][j])
            cols.append(e)
        rows.append(cols)

    # enter separator labels
    for i in range(n_value):
        Label(parametric_root, text='< =').grid(row=i + 4, column=8)

    right_vector = [40 - t, 60 + 2*t, 30 - 7*t]
    # enter right side constraint vector
    vec_rows = []
    for i in range(n_value):
        e = Entry(parametric_root, relief=RIDGE)
        e.grid(row=i + 4, column=9, sticky=NSEW, padx=5, pady=5)
        e.insert(END, right_vector[i])
        vec_rows.append(e)

    Label(parametric_root, text='right side vector').grid(row=3, column=9)
    z_indice = i + 5
    Label(parametric_root, text='right side vector').grid(row=z_indice, column=0)

    # enter z function vector
    z_init = [3, 2, 5]
    # z_init = [1, 1, 1]
    z_rows = []
    for j in range(m_value):
        e = Entry(parametric_root, relief=RIDGE)
        e.grid(row=z_indice + 1, column=j, sticky=NSEW, padx=5, pady=5)
        e.insert(END, z_init[j])
        z_rows.append(e)

    x1 = [[0] * len(rows) for x in range(len(rows))]
    x_b = [0 for x in range(len(rows))]
    z_array = [0 for x in range(len(rows))]

    strategies_recovered = [0 for x in range(len(x1))]

    v_recovered = StringVar()
    # v_label_msg = Label(parametric_root, text='Game value = ').grid(row=11, column=0)
    # v_label = Label(parametric_root, textvariable=v_recovered).grid(row=11, column=1)
    #
    # s_label = Label(parametric_root, textvariable=strategies_recovered).grid(row=12, column=0)
    #
    # p_label_msg = Label(parametric_root, text='game strategy values = ').grid(row=14, column=0)

    p_recovered = [StringVar() for x in range(m_value)]
    for i in range(m_value):
        p_label = Label(parametric_root, textvariable=p_recovered[i]).grid(row=14, column=i + 1)

    parametric_array = [0 for x in range(len(x1))]

    def get_x_1():
        i = 0
        for row in rows:
            j = 0
            for col in row:
                x1[i][j] = parse_expr(col.get())
                j += 1
            i += 1
        return x_1

    def get_x_b():
        v = 0
        for vec in vec_rows:
            x_b[v] = parse_expr(vec.get())
            v += 1
        return x_b

    def get_z_init():
        v = 0
        for vec in z_rows:
            z_array[v] = parse_expr(vec.get())
            v += 1
        return z_array

    def on_press():
        k = parse_expr(k1.get())
        t_value = parse_expr(t1.get())
        parametric_array = [0 for x in range(len(x1))]
        #parametric_simplex_solution(get_x_1(), get_x_b(), k, t_value, parametric_array)
        #v_recovered.set(str(1/sum(parametric_array)))
        # for p in range(m_value):
        #     p_recovered[p].set(parametric_array[p])
        one_window(parametric_root, get_x_1(), get_x_b(), get_z_init(), k, t_value)

    def on_extended_press():
        k = parse_expr(k1.get())
        t_value = parse_expr(t1.get())
        report_window(parametric_root, get_x_1(), get_x_b(), k, t_value)

    Button(parametric_root, text='Solve', command=on_press).grid(row=30, column=9, padx=10, pady=10)

    Button(parametric_root, text='Get extended report', command=on_extended_press).grid(row=33, column=9, padx=10, pady=10)

    parametric_root.mainloop()
