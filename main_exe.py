#http://www.python-course.eu/tkinter_entry_widgets.php
from tkinter import *
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

t = Symbol('t')

# finds largest value
def find_largest_value(data):
    maximum = 0
    m, location = 0, 0
    maximum = data[0]

    for m in range(1, len(data)):
        if data[m] > maximum:
            maximum = data[m]
            location = m

    return location


# finds entering column
# column ==> in
def find_entering_column(data):
    max_negative = min([n for n in data if n < 0])

    if max_negative >= 0:
        return - 1

    for m in range(1, len(data)):
        if data[m] == max_negative:
            return m


# finds departing row
#  returns number
def find_departing_row(table, pivot_column):
    rows = len(table)
    values = [0 for x in range(rows - 1)]

    for i in range(1, rows):
        if table[i][pivot_column] > 0:
            values[i - 1] = table[i][0] / table[i][pivot_column]
        else:
            values[i - 1] = -1

    min_value = min([n for n in values if n >= 0])
    pivot_row = 0
    for i in range(0, rows):
        if values[i] == min_value:
            return i + 1


#generate next table
def form_next_table(table, pivot_row, pivot_column):

    columns = len(table[0])
    rows = len(table)

    pivot_value = table[pivot_row][pivot_column]

    pivot_vector = [0 for x in range(columns)]
    for j in range(0, columns):
        pivot_vector[j] = table[pivot_row][j] / pivot_value
        table[pivot_row][j] = pivot_vector[j]

    for i in range(0, rows):
        ratio = table[i][pivot_column]
        if i == pivot_row:
            continue
        for j in range(0, columns):
            multiplier = pivot_vector[j] * ratio
            table[i][j] -= multiplier

    return table


# main simplex method
def simplex_mher(table):

    columns = len(table[0])
    rows = len(table) - 1

    array = table[0]
    pivot_column = find_entering_column(array)
    pivot_row = find_departing_row(table, pivot_column)

    print("pivot column", pivot_column)
    print("pivot row", pivot_row)

    while pivot_column >= 0:
        table = form_next_table(table, pivot_row, pivot_column)


        if not any([n for n in array if n < 0]):
            break

        array = table[0]
        pivot_column = find_entering_column(array)
        pivot_row = find_departing_row(table, pivot_column)

    return table


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


def help_window(root):
    help_root = Toplevel(root)
    help_root.title("Applied package guide")
    help_root.geometry("800x600")

    # top level bar
    Label(help_root, text=' Guide to use software ').grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    Label(help_root, text=' ---------------------------------------- ').grid(row=1, column=0, padx=10, pady=10)
    Label(help_root, text=' All the parametric expressions should be entered '
                          'to the system by strictly following this rules!!! ').grid(row=2, column=0, padx=10, pady=10)

    help_root.mainloop()


d = Symbol('d')
t = Symbol('t')
# k = 2
# d_value = 0.5
# t_value = 1.55

w1 = 0.4
w2 = 0.4
w3 = 0.4


R_matrix = [[(0.4 * ((7/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((7.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((4/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((4.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((13.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((7.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((8/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((8.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((10/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((10.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((4/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((4.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((13/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((12.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((9.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((4/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((4.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((10/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((10.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((14.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((9.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((5/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((7.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((10.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((15/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((15.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((10/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((10.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((8/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((7.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((11/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((7.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((4.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((17/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((13.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((8/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((13/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((17.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((4/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((5.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((7.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((4/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((13.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((7.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((12/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((12.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((7.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((14.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((9.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((4/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((14.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((15/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((15.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((10.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((8/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.3/d)** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((14.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((7.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((13.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((18/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((18.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((7/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((7.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((9/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((9.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((16/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((15.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((15.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((17/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((17.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((13/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((13.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((12/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((11.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((8/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.3/d) ** 2)) ** -0.5 ],

            [(0.4 * ((7/d) ** 2) + 0.4 * ((0.7/t) ** 2) + 0.4 * ((7.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((3/d) ** 2) + 0.4 * ((0.5/t) ** 2) + 0.4 * ((2.2/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((6.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((11/d) ** 2) + 0.4 * ((1.6/t) ** 2) + 0.4 * ((11.1/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((9.4/d) ** 2)) ** -0.5 ,
             (0.4 * ((14/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((13.9/d) ** 2)) ** -0.5 ,
             (0.4 * ((9/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.6/d) ** 2)) ** -0.5 ,
             (0.4 * ((8/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((8.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((5/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((5.3/d) ** 2)) ** -0.5 ,
             (0.4 * ((6/d) ** 2) + 0.4 * ((0.6/t) ** 2) + 0.4 * ((7.3/d) ** 2)) ** -0.5 ]]


def item_multi_transform(item, t_level, d_level, t_value, d_value):
    if t_level == 0 and d_level == 0:
        return item.evalf(subs={t: t_value, d: d_value})
    if t_level == 0:
        d_derive = diff(item, d, d_level)
        return d_derive.evalf(subs={t: t_value, d: d_value})
    if d_level == 0:
        d_derive = diff(item, t, t_level)
        return d_derive.evalf(subs={t: t_value, d: d_value})
    derivative = diff(item, t, t_level)
    d_derive = diff(derivative, d, d_level)
    expr_with_value = d_derive.evalf(subs={t: t_value, d: d_value})
    return expr_with_value


def matrix_multi_differential(matrix, t_level, d_level, t_value, d_value):
    "returns a differential of given matrix"
    _length = len(matrix)
    z_matrix = [[0] * _length for x in range(_length)]
    for i in range(0, _length):
        for j in range(0, _length):
            z_matrix[i][j] = item_multi_transform(matrix[i][j], t_level, d_level, t_value, d_value)
    return z_matrix


def prepare_matrix_for_simplex(s_matrix, k1, k2, t_value, d_value):
    simplex_matrix = []
    _length = len(s_matrix)
    z = []
    z.append(0.0)
    if_zero_step = k1 == 0 and k2 == 0
    for z_i in range(0, _length):
        if if_zero_step:
            z.append(-1.0)
        else:
            z.append(0.0)
    for z_i in range(0, _length):
        z.append(0.0)
    simplex_matrix.append(z)
    base_matrix = matrix_multi_differential(s_matrix, k1, k2, t_value, d_value)
    for m_i in range(0, _length):
        m_array = [0 for var in range(_length * 2 + 1)]
        for m_j in range(0, _length):
            if if_zero_step:
                m_array[0] = 1.0
            else:
                m_array[0] = 0.0
            m_array[m_j + 1] = base_matrix[m_i][m_j]
            if m_i == m_j and if_zero_step:
                m_array[_length + m_j + 1] = 1.0
            else:
                m_array[_length + m_j + 1] = 0.0
        simplex_matrix.append(m_array)
    return simplex_matrix


def get_image_matrixes(s_matrix, k1_value, k2_value, d_value, t_value):

    simplex_matrix = prepare_matrix_for_simplex(s_matrix, 0, 0, t_value, d_value)

    image_matrixes = [simplex_matrix * (k1_value + 1) for x in range(k2_value + 1)]
    for i in range(0, k1_value + 1):
        for j in range(0, k2_value + 1):
            image_matrixes[i][j] = prepare_matrix_for_simplex(s_matrix, i, j, t_value, d_value)
    return image_matrixes


def next_simplex_table(table, pivot_row, pivot_column, pivot_value, ratio_vec):

    columns = len(table[0])
    rows = len(table)

    pivot_vector = [0 for x in range(columns)]
    for j in range(0, columns):
        pivot_vector[j] = table[pivot_row][j] / pivot_value
        table[pivot_row][j] = pivot_vector[j]

    for i in range(0, rows):
        ratio = table[i][pivot_column]
        ratio_vec[i] = ratio
        if i == pivot_row:
            continue
        for j in range(0, columns):
            multiplier = pivot_vector[j] * ratio
            table[i][j] -= multiplier

    return table


def simplex_multi(table, image_matrixes, k1_value, k2_value):

    columns = len(table[0])
    rows = len(table)

    array = table[0]
    pivot_column = find_entering_column(array)
    pivot_row = find_departing_row(table, pivot_column)

    print("pivot column", pivot_column)
    print("pivot row", pivot_row)

    while pivot_column >= 0:

        pivot_value = table[pivot_row][pivot_column]
        ratio_vec = [0 for x in range(rows)]
        table = next_simplex_table(table, pivot_row, pivot_column, pivot_value, ratio_vec)

        for k1 in range(0, k1_value + 1):
            for k2 in range(0, k2_value + 1):
                # pivot image row
                image_matrix = image_matrixes[k1][k2]
                image_matrixes[k1][k2] = next_image_table(image_matrix, pivot_row, pivot_column, pivot_value, ratio_vec)



        if not any([n for n in array if n < 0]):
            break

        array = table[0]
        pivot_column = find_entering_column(array)
        pivot_row = find_departing_row(table, pivot_column)

    return table


def next_image_table(table, pivot_row, pivot_column, pivot_value, ratio_vec):

    columns = len(table[0])
    rows = len(table)

    # pivot row
    pivot_vector = [0 for x in range(columns)]
    for j in range(0, columns):
        pivot_vector[j] = table[pivot_row][j] / pivot_value
        table[pivot_row][j] = pivot_vector[j]

    for i in range(0, rows):
        if i == pivot_row:
            continue
        for j in range(0, columns):
            multiplier = pivot_vector[j] * ratio_vec[i]
            table[i][j] -= multiplier

    return table


def initiate_simplex_matrix(s_matrix, v_recovered, strategies_recovered, parametric_array, k1_value, k2_value, d_value, t_value):

    image_matrixes = get_image_matrixes(s_matrix, k1_value, k2_value, t_value, d_value)
    simplex_matrix = prepare_matrix_for_simplex(s_matrix, 0, 0, t_value, d_value)

    tableu = simplex_multi(simplex_matrix, image_matrixes, k1_value, k2_value)
    image_matrixes[0][0] = tableu

    return image_matrixes


def multy_window(root, s_matrix, k1_value, k2_value, d_value, t_value):
    mul_root = Toplevel(root)
    mul_root.title("game model solution")
    mul_root.geometry("1200x800")

    # top level bar
    # Label(mul_root, text=' K ').grid(row=0, column=0)
    solution_matrix = initiate_simplex_matrix(R_matrix, [], [], [], k1_value, k2_value, d_value, t_value)

    rows = len(s_matrix)

    x_parametric_array = [0 for x in range(rows)]
    y_parametric_array = [0 for x in range(rows)]

    z_parametric_array = [0 for x in range(rows*2)]

    function_max_parametric = 0
    for k1 in range(0, k1_value + 1):
        for k2 in range(0, k2_value + 1):
            current_image_table = solution_matrix[k1][k2]
            table_len = len(current_image_table[0])
            for i in range(rows):
                indice = int((table_len - 1) / 2) + 1
                y_parametric_array[i] += current_image_table[0][indice + i]*((t-t_value)**k1)*((d-d_value)**k2)
                item = current_image_table[i][0]
                if item > 0 and i > 0:
                    x_parametric_array[i - 1] += item*((t-t_value)**k1)*((d-d_value)**k2)

            for j in range(1, table_len):
                z_parametric_array[j - 1] += current_image_table[0][j]*((t-t_value)**k1)*((d-d_value)**k2)

            f_image = current_image_table[0][0]
            function_max_parametric += f_image*((t-t_value)**k1)*((d-d_value)**k2)

    print(' parametric F max = ', function_max_parametric)
    game_value = 1/function_max_parametric
    print(' parametric Game value = ', game_value)

    print(' y_parametric array = ', y_parametric_array)
    print(' x_parametric array = ', x_parametric_array)
    print(' z_parametric_array array = ', z_parametric_array)

    x_probability = [x * game_value for x in x_parametric_array]
    y_probability = [x * game_value for x in y_parametric_array]
    print('x_probability array = ', x_probability)
    print('y_probability array = ', y_probability)

    # res = multy_nonlinear_optimality(z_parametric_array, d_value, t_value)
    # print("optimality = ", res)

    Label(mul_root, text=" Game Value = "+ str(game_value)).grid(row=k1_value + 2, column=1)
    Label(mul_root, text=" X probabilities = " + str(x_probability)).grid(row=k1_value + 3, column=1)
    Label(mul_root, text=" Y probabilities = " + str(y_probability)).grid(row=k1_value + 4, column=1)

    # for i in range(len(x_probability)):
    #     label_indice = " X probabilities"

    mul_root.mainloop()



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
    d.insert(END, 2.5)

    Label(multi_root, text='approximation center t=').grid(row=3, column=2)
    t = Entry(multi_root, relief=RIDGE)
    t.grid(row=3, column=3, sticky=NSEW, padx=5, pady=5)
    t.insert(END, 106)

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

def create_cooperative_window():
    n_value = parse_expr(n.get())
    m_value = parse_expr(m.get())
    cooperative_window(root, n_value, m_value)


def create_multi_parameter_window():
    n_value = parse_expr(n.get())
    m_value = parse_expr(m.get())
    multi_window(root, n_value, m_value)


def create_help_window():
    help_window(root)


Button(root, text='Cooperative game', command=create_cooperative_window).grid(padx=10, pady=10)
Button(root, text='Multi parameter game', command=create_multi_parameter_window).grid(padx=10, pady=10)
Button(root, text='Help', command=create_help_window).grid(padx=10, pady=10)

root.mainloop()







