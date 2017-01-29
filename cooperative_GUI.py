# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from cooperative import *
from tkinter import *
from sympy.parsing.sympy_parser import parse_expr


def cooperative_window(root, n_value, m_value):
    cooperative_root = Toplevel(root)
    cooperative_root.title("Cooperative game model solver")
    cooperative_root.geometry("800x600")

    Label(cooperative_root, text='K').grid(row=0, column=1)
    k1 = Entry(cooperative_root, relief=RIDGE)
    k1.grid(row=0, column=2, sticky=NSEW, padx=5, pady=5)
    k1.insert(END, 2)

    Label(cooperative_root, text='Sympathy parameter = ').grid(row=0, column=3)
    s1 = Entry(cooperative_root, relief=RIDGE)
    s1.grid(row=0, column=4, sticky=NSEW, padx=5, pady=5)
    s1.insert(END, 0.1)

    Label(cooperative_root, text='approximation center t=').grid(row=3, column=1)
    t1 = Entry(cooperative_root, relief=RIDGE)
    t1.grid(row=3, column=2, sticky=NSEW, padx=5, pady=5)
    t1.insert(END, 1.55)

    Label(cooperative_root, text='iterations count = ').grid(row=3, column=4)
    i_entry = Entry(cooperative_root, relief=RIDGE)
    i_entry.grid(row=3, column=4, sticky=NSEW, padx=5, pady=5)
    i_entry.insert(END, 1)

    # enter matrix
    rows = []
    for i in range(n_value):
        cols = []
        for j in range(m_value):
            e = Entry(cooperative_root, relief=RIDGE)
            e.grid(row=i + 4, column=j, sticky=NSEW, padx=5, pady=5)
            e.insert(END, 0.0)
            cols.append(e)
        rows.append(cols)

    z_matrix = [[0] * len(rows) for x in range(len(rows))]

    # p_recovered = [[StringVar()] * m_value for x in range(n_value)]
    #
    # p_recovered[0][0].set('1')
    # p_recovered[0][1].set('2')
    # p_recovered[1][0].set('3')
    # p_recovered[1][1].set('4')
    #
    # for i in range(n_value):
    #     for j in range(m_value):
    #         Label(cooperative_root, textvariable=p_recovered[i][j]).grid(row=10 + i, column=j)

    p_recovered = [StringVar() for x in range(m_value)]
    for i in range(m_value):
        Label(cooperative_root, textvariable=p_recovered[i]).grid(row=10 + i, column=1)

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

            iterations = parse_expr(i_entry.get())
            k = parse_expr(k1.get())
            t_value = parse_expr(t1.get())
            sympathy = parse_expr(s1.get())

        result = cooperative_matrix(z_matrix, iterations, k, t_value, sympathy)

        # for i in range(0, n_value):
        #     for j in range(0, m_value):
        #         p_recovered[i][j].set(result[i][j])
        for i in range(0, m_value):
            p_recovered[i].set(result[i])

    Button(cooperative_root, text='Solve', command=on_press).grid(row=20, column=4)
    cooperative_root.mainloop()
