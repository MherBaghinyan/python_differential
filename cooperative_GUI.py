# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from Multiparametric import *
from tkinter import *
from sympy.parsing.sympy_parser import parse_expr

root = Tk()
root.title("Cooperative game model solver")
root.geometry("1100x700")

Label(root, text='N=').grid(row=0, column=0)
n = Entry(root, relief=RIDGE)
n.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5)
n.insert(END, 2)
Label(root, text='M=').grid(row=1, column=0)
m = Entry(root, relief=RIDGE)
m.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5)
m.insert(END, 2)

Label(root, text='K').grid(row=0, column=2)
k1 = Entry(root, relief=RIDGE)
k1.grid(row=0, column=3, sticky=NSEW, padx=5, pady=5)
k1.insert(END, 0)

Label(root, text='approximation center t=').grid(row=3, column=2)
t = Entry(root, relief=RIDGE)
t.grid(row=3, column=3, sticky=NSEW, padx=5, pady=5)
t.insert(END, 0.1)

# enter matrix
rows = []
for i in range(2):
    cols = []
    for j in range(2):
        e = Entry(root, relief=RIDGE)
        e.grid(row=i + 4, column=j, sticky=NSEW, padx=5, pady=5)
        e.insert(END, 0.0)
        cols.append(e)
    rows.append(cols)

v_recovered = ''
z_matrix = [[0] * len(rows) for x in range(len(rows))]

strategies_recovered = [0 for x in range(len(z_matrix))]

v_label = Label(root, text=v_recovered).grid(row=11, column=0)

s_label = Label(root, text=strategies_recovered).grid(row=12, column=0)


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
