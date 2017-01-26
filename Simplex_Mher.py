def printTableu(tableu):
     print('----------------------')
     for row in tableu:
      print (row)
     print('----------------------')
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
    location = 0
    max_negative = min([n for n in data if n < 0])

    if max_negative >= 0:
        return - 1

    for m in range(1, len(data)):
        if data[m] == max_negative:
            location = m
            return location


# finds departing row
#  returns number
def find_departing_row(table, pivot_column):
    rows = len(table)
    values = [0 for x in range(rows - 1)]

    for i in range(1, rows):
        if table[i][pivot_column] > 0:
            values[i - 1] = table[i][0] / table[i][pivot_column]
        else:
            values[i - 1] = 0

    max_value = min([n for n in values if n >= 0])
    pivot_row = 0
    for i in range(0, rows):
        if values[i] == max_value:
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


#main simplex method
def simplex_mher(table):

    columns = len(table[0])
    rows = len(table) - 1

    array = table[0]
    pivot_column = find_entering_column(array)
    pivot_row = find_departing_row(table, pivot_column)

    print("pivot column", pivot_column)
    print("pivot row", pivot_row)

    table = form_next_table(table, pivot_row, pivot_column)
    print(table)


tableu = []
z = [0.0, -1.0, -1.0, -1.0, 0.0,  0.0,  0.0]
x1 = [1.1504, 179.95 ,  156.12 , 90 ,  1.0,  0.0,  0.0]
x2 = [1.1504, 89.95 , 179.87 , 155 ,   0.0,  1.0,  0.0]
x3 = [1.1504, 180,  156 , 177 ,  0.0,  0.0,  1.0]

tableu.append(z)
tableu.append(x1)
tableu.append(x2)
tableu.append(x3)

tableu = simplex_mher(tableu)

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
