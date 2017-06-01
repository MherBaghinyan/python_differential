from project_files.services.transformation_util import *

def printTableu(tableu):
     print('----------------------')
     for row in tableu:
      print (row)
     print('----------------------')
     return


def write_table_file(table):
    with open("Output.txt", "a") as text_file:
        print('----------------------', file=text_file)
    for row in table:
        with open("Output.txt", "a") as text_file:
            print(row, file=text_file)

    return


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
def simplex_main(table):

    columns = len(table[0])
    rows = len(table) - 1

    array = table[0]
    pivot_column = find_entering_column(array)
    pivot_row = find_departing_row(table, pivot_column)

    print("pivot column", pivot_column)
    print("pivot row", pivot_row)

    while pivot_column >= 0:
        table = form_next_table(table, pivot_row, pivot_column)
        printTableu(table)

        if not any([n for n in array if n < 0]):
            break

        array = table[0]
        pivot_column = find_entering_column(array)
        pivot_row = find_departing_row(table, pivot_column)

    return table

    # s_matrix = [[179.95 + t, 156.12*d + t**2, d*(1-0.2*t)],
    #             [89.95 + sqrt(d + 1), 160 + 1/d, 90*t + d],
    #             [180*t + (d + t), 156 + 5 + d, 77*t**3]]

# s_matrix = [[sin(t), 1/(t**2), 0.8 + d**3, d*(1-0.2*t) + 1],
#             [2*t / ((d + 1) ** 3) ** -0.5, 90*t/2 + d, acos(1/t), exp(t + d)],
#             [4/(d+t), 5 + d, 155*t, sqrt(d**2 + t) + 4],
#             [t**3, acos(t) + atan(d), (d**3)/cos(2 * t), tanh(4*exp(d))]]
#
#     s_matrix = [[179.95 + t, 156.12*d + t**2, d*(1-0.2*t), 60*t + 5*d],
#                 [89.95 + (d**2 + 1)/2, 160 + 1/d, 90*t + d, 7/t + 58.7],
#                 [155, 120 + 1/(2*t + d), t + (d - 1)**2, 120],
#                 [180*t + (d + t), 156 + 5 + d, 77*t**3, 162 + t/(d-7)]]

# tableu = []
# z = [0.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0]
# x1 = [1, 1 + t, 2 * d, 1, 1.0, 0.0, 0.0]
# x2 = [1, 3 - 2 * t, d, 2, 0.0,  1.0, 0.0]
# x3 = [1, 1 + 3 * t, 4, d, 0.0, 0.0,  1.0]


tableu = []
z = [0.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0]
x1 = [1, 1 + 0, 2 * 0, 1, 1.0, 0.0, 0.0]
x2 = [1, 3 - 2 * 0, 0, 2, 0.0,  1.0, 0.0]
x3 = [1, 1 + 3 * 0, 4, 0, 0.0, 0.0,  1.0]


tableu.append(z)
tableu.append(x1)
tableu.append(x2)
tableu.append(x3)

tableu = simplex_main(tableu)
#
print("Fmax = ", tableu[0][0])
V = 1/tableu[0][0]
print("V = ", V)
#
print("x1= ", V * tableu[1][0])
print("x2= ", V * tableu[2][0])
print("x3= ", V * tableu[3][0])


print("=-------------")
# z = [0.0, -3.0, -2.0, -5.0, 0.0,  0.0,  0.0]
# x_b = [40.0, 60.0, 30.0]
# x1 = [1.0 ,  2.0 , 1.0 ,  1.0,  0.0,  0.0]
# x2 = [3.0 , 0.0, 2.0,   0.0,  1.0,  0.0]
# x3 = [1.0,  4.0 , 0.0 ,  0.0,  0.0,  1.0]

# z = [0.0, -1.0, -1.0, -1.0, 0.0,  0.0,  0.0]
# x_b = [1.1504, 1.1504, 1.1504]
# x1 = [179.95 ,  156.12 , 90 ,  1.0,  0.0,  0.0]
# x2 = [89.95 , 179.87 , 155 ,   0.0,  1.0,  0.0]
# x3 = [180,  156 , 177 ,  0.0,  0.0,  1.0]
#
# tableu = []
# tableu.append(z)
# tableu.append(x1)
# tableu.append(x2)
# tableu.append(x3)
