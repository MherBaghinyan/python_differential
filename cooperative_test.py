#http://www.python-course.eu/tkinter_entry_widgets.php
from tkinter import *
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

t = Symbol('t')


def exponential_matrix(matrix_a, matrix_b, k, t_value, sympathy):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    e_matrix = [[0] * columns for x in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            item1 = matrix_a[i][j]
            item2 = matrix_b[i][j]
            if is_number(item1):
                multiplied = float(item1*exp(-sympathy*(item1 - item2)))
                # formatted = float("{0:.5f}".format(multiplied))
                e_matrix[i][j] = multiplied
            else:
                e_matrix[i][j] = recover_exponential_image_values(item1, exp(-sympathy*(item1 - item2)), k, t_value)
    return e_matrix


# def multiply_image_matrix(matrix, k):
#     _length = len(matrix)
#     z_matrix = [[0] * _length for x in range(_length)]
#     for l in range(0, k + 1):
#         z_matrix += np.dot(differential_transform(matrix, l), differential_transform(matrix, k - l))
#     return z_matrix


def item_transformation(item, level, t_value):
    derivative = diff(item, t, level)
    expr_with_value = derivative.evalf(subs={t: t_value})
    return expr_with_value / factorial(level)


def multiply_images(value1, value2, k_value, t_value):
    value = 0
    for l in range(0, k_value + 1):
        value += item_transformation(value1, k_value - l, t_value) * item_transformation(value2, k_value, t_value)
    return value


def exponential_c_values(image1, image2, k_value, t_value):
    item = 0
    if k_value == 0:
        return 1/multiply_images(image1, image2, 0, t_value)
    for k in range(0, k_value):
        item += exponential_c_values(image1, image2, k, t_value)*multiply_images(image1, image2, k_value - k, t_value)
    return (1/multiply_images(image1, image2, 0, t_value))*(1/factorial(k_value) - item)


def recover_exponential_image_values(image1, image2, k_value, t_value):
    item = 0
    for k in range(0, k_value + 1):
        item += (t-t_value) ** k * exponential_c_values(image1, image2, k, t_value)
    return exp(t-t_value)/item


def set_value_to_matrix(matrix, t_value):
    rows = len(matrix)
    columns = len(matrix[0])
    e_matrix = [[0] * columns for x in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            item = matrix[i][j]
            if is_number(item):
                e_matrix[i][j] = item
            else:
                e_matrix[i][j] = item.evalf(subs={t: t_value})
    print(e_matrix)
    return e_matrix


def get_matrix_b(matrix_a):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    b_matrix = [[0] * columns for x in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            item = matrix_a[i][j]
            if i == j:
                b_matrix[i][j] = item
            else:
                b_matrix[i][j] = -item
    return b_matrix


def cooperative_matrix(matrix, iterations, k, t_value_, sympathy):
    t_value = t_value_
    for iteration in range(0, iterations):
        matrix_a = matrix
        matrix_b = get_matrix_b(matrix_a)
        matrix = exponential_matrix(matrix_a, matrix_b, k, t_value, sympathy)
        print(matrix)

    return matrix


def is_number(s):
    try:
        float(s)
        return True
    except TypeError:
        return False


def graph_c_window(root, matrix, t_value):
    graph_c_root = Toplevel(root)
    graph_c_root.title("cooperative game report")
    graph_c_root.geometry("900x700")

    xf = Frame(graph_c_root, relief=GROOVE, borderwidth=2)
    Label(graph_c_root, text='parametric values of cooperation matrix ').place(relx=0.1, rely=0.10, anchor=NW)
    xf.place(relx=0.1, rely=0.145, anchor=NW)


    # enter matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            Label(xf, text=str(matrix[i][j]), relief=GROOVE).grid(row=i + 1, column=j + 1, padx=10, pady=10)

    pf = Frame(graph_c_root, relief=GROOVE, borderwidth=2)
    pf.place(relx=0.1, rely=0.325, anchor=NW)

    Label(graph_c_root, text='numerical values of cooperation matrix in  t = ' + str(t_value) + '').place(relx=0.1, rely=0.29, anchor=NW)

    value_matrix = set_value_to_matrix(matrix, t_value)

    for i in range(len(value_matrix)):
        for j in range(len(value_matrix)):
            Label(pf, text=str(value_matrix[i][j]), relief=RAISED, anchor=W).grid(row=i + 2 + len(matrix), column=j + 1, padx=10, pady=10)

    graph_c_root.mainloop()


def cooperative_window(root, n_value, m_value):
    cooperative_root = Toplevel(root)
    cooperative_root.title("Cooperative game model solver")
    cooperative_root.geometry("800x600")

    Label(cooperative_root, text='N = ').grid(row=0, column=0)
    Label(cooperative_root, text=n_value).grid(row=0, column=1)
    Label(cooperative_root, text='M = ').grid(row=1, column=0)
    Label(cooperative_root, text=m_value).grid(row=1, column=1)

    Label(cooperative_root, text='K').grid(row=0, column=2)
    k1 = Entry(cooperative_root, relief=RIDGE)
    k1.grid(row=0, column=3, sticky=NSEW, padx=5, pady=5)
    k1.insert(END, 2)

    Label(cooperative_root, text='approximation center t=').grid(row=1, column=2)
    t1 = Entry(cooperative_root, relief=RIDGE)
    t1.grid(row=1, column=3, sticky=NSEW, padx=5, pady=5)
    t1.insert(END, 1.55)

    Label(cooperative_root, text='Sympathy parameter = ').grid(row=4, column=2)
    s1 = Entry(cooperative_root, relief=RIDGE)
    s1.grid(row=4, column=3, sticky=NSEW, padx=5, pady=5)
    s1.insert(END, 0.1)

    Label(cooperative_root, text='enter parametric game matrix').grid(row=5, column=0)

    # enter matrix
    rows = []
    for i in range(n_value):
        cols = []
        for j in range(m_value):
            e = Entry(cooperative_root, relief=RIDGE)
            e.grid(row=i + 6, column=j, sticky=NSEW, padx=5, pady=5)
            e.insert(END, 0.0)
            cols.append(e)
        rows.append(cols)

    z_matrix = [[0] * len(rows) for x in range(len(rows))]

    p_recovered = [StringVar() for x in range(m_value)]
    i = 0
    for i in range(m_value):
        Label(cooperative_root, textvariable=p_recovered[i]).grid(row=10 + i, column=1)

    p_values = [StringVar() for x in range(m_value)]
    for j in range(m_value):
        Label(cooperative_root, textvariable=p_values[j]).grid(row=10 + i + j, column=1)

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

            # iterations = parse_expr(i_entry.get())
            k = parse_expr(k1.get())
            t_value = parse_expr(t1.get())
            sympathy = parse_expr(s1.get())

        result = cooperative_matrix(z_matrix, 1, k, t_value, sympathy)

        # for i in range(0, m_value):
        #     p_recovered[i].set(result[i])
        #
        # for j in range(0, m_value):
        #     p_values[i].set(set_value_to_matrix(result, t_value))

        graph_c_window(cooperative_root, result, t_value)

    Button(cooperative_root, text='Solve', command=on_press).grid(row=20, column=4)
    cooperative_root.mainloop()

root = Tk()
root.title("Parametric game model solver")
root.geometry("360x300")

n_value = 2
m_value = 2

Label(root, text='Enter payoff matrix metrics').grid(row=1, column=0)

Label(root, text='N=').grid(row=2, column=0)
n = Entry(root, relief=RIDGE)
n.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)
n.insert(END, n_value)
Label(root, text='M=').grid(row=3, column=0)
m = Entry(root, relief=RIDGE)
m.grid(row=3, column=1, sticky=NSEW, padx=5, pady=5)
m.insert(END, m_value)


def create_cooperative_window():
    n_value = parse_expr(n.get())
    m_value = parse_expr(m.get())
    cooperative_window(root, n_value, m_value)

Button(root, text='Cooperative game', command=create_cooperative_window).grid(padx=10, pady=10)

root.mainloop()







