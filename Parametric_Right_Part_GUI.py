# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from Multiparametric import *
from Simplex_Parametric_Right import *
from tkinter import *
from sympy.parsing.sympy_parser import parse_expr


def parametric_window(root, n_value, m_value):
    parametric_root = Toplevel(root)
    parametric_root.title("Cooperative game model solver")
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

    # enter matrix
    rows = []
    for i in range(n_value):
        cols = []
        for j in range(m_value):
            e = Entry(parametric_root, relief=RIDGE)
            e.grid(row=i + 4, column=j, sticky=NSEW, padx=5, pady=5)
            e.insert(END, 0.0)
            cols.append(e)
        rows.append(cols)

    # enter separator labels
    for i in range(n_value):
        Label(parametric_root, text='< =').grid(row=i + 4, column=8)


    # enter right side constraint vector
    vec_rows = []
    for i in range(n_value):
        e = Entry(parametric_root, relief=RIDGE)
        e.grid(row=i + 4, column=9, sticky=NSEW, padx=5, pady=5)
        e.insert(END, 0.0)
        vec_rows.append(e)

    Label(parametric_root, text='right side vector').grid(row=3, column=9)

    x1 = [[0] * len(rows) for x in range(len(rows))]
    x_b = [0 for x in range(len(rows))]

    strategies_recovered = [0 for x in range(len(x1))]

    v_recovered = StringVar()
    v_label_msg = Label(parametric_root, text='Game value = ').grid(row=11, column=0)
    v_label = Label(parametric_root, textvariable=v_recovered).grid(row=11, column=1)

    s_label = Label(parametric_root, textvariable=strategies_recovered).grid(row=12, column=0)

    p_label_msg = Label(parametric_root, text='game strategy values = ').grid(row=14, column=0)

    p_recovered = [StringVar() for x in range(m_value)]
    for i in range(m_value):
        p_label = Label(parametric_root, textvariable=p_recovered[i]).grid(row=14, column=i + 1)

    parametric_array = [0 for x in range(len(x1))]

    def on_press():
        i = 0
        for row in rows:
            j = 0
            for col in row:
                x1[i][j] = parse_expr(col.get())
                j += 1
                print(col.get())
            i += 1
            print()

        v = 0
        for vec in vec_rows:
            x_b[v] = parse_expr(vec.get())
            v += 1
            print(vec.get())

        k = parse_expr(k1.get())
        t_value = parse_expr(t1.get())

        x_1 = [[179.95, 156.12, 90],
              [89.95, 179.87, 155],
              [180, 156, 177]]

        game_value = parametric_simplex_solution(x_1, x_b, k, t_value, strategies_recovered, parametric_array)
        v_recovered.set(game_value)
        for p in range(m_value):
            p_recovered[p].set(parametric_array[p])

    Button(parametric_root, text='Solve', command=on_press).grid(row=30, column=9)
    parametric_root.mainloop()
