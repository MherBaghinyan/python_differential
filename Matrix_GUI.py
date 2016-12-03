# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from Multiparametric import *
from tkinter import *
from sympy.parsing.sympy_parser import parse_expr

root = Tk()
root.title("Multi Parametric game model solver")
root.geometry("700x700")


rows = []
for i in range(5):
    cols = []
    for j in range(5):
        e = Entry(root, relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, 0.0)
        cols.append(e)
    rows.append(cols)

v_recovered = ''
z_matrix = [[0] * len(rows) for x in range(len(rows))]

strategies_recovered = [0 for x in range(len(z_matrix))]

v_label = Label(root, text=v_recovered).grid(row=0, column=6)

s_label = Label(root, text=strategies_recovered).grid(row=1, column=7)

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
    v_recovered = initiate_simplex_matrix(z_matrix, recover_value, strategies_recovered)


Button(root, text='Solve', command=on_press).grid()
mainloop()
