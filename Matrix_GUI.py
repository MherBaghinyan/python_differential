# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from Multiparametric import *
from tkinter import *
from sympy.parsing.sympy_parser import parse_expr

rows = []
for i in range(5):
    cols = []
    for j in range(5):
        e = Entry(relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, 0.0)
        cols.append(e)
    rows.append(cols)


def on_press():
    z_matrix = [[0] * len(rows) for x in range(len(rows))]
    i = 0
    for row in rows:
        j = 0
        for col in row:
            z_matrix[i][j] = parse_expr(col.get())
            j += 1
            print(col.get())
        i += 1
        print()

    v_recovered = 0
    strategies_recovered = [0 for x in range(len(z_matrix))]
    v_recovered = initiate_simplex_matrix(z_matrix, v_recovered, strategies_recovered)

    v_label = Label(text=v_recovered)
    v_label.pack()
    s_label = Label(text=strategies_recovered)
    s_label.pack()

Button(text='Fetch', command=on_press).grid()
mainloop()
