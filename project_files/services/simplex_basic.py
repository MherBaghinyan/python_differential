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
# d=2.5
# tableu = []
# z = [0.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# x1= [1.0, 0.396446212399178, 0.681500034988213, 0.454339433915631, 0.252933019899052, 0.537101359844810, 0.200362300489902, 0.317537604750414, 0.542486488956359, 0.239811667469510, 0.418311541037243, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# x2= [1.0, 0.347202264023728, 0.276725827625413, 0.454339433915631, 0.689822784443095, 0.537101359844810, 0.243922243818781, 0.317537604750414, 0.220869568436793, 0.339586660431072, 0.454339433915631, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# x3= [1.0, 0.690040324043369, 0.276725827625413, 0.454339433915631, 0.198930723087575, 0.537101359844810, 0.243922243818781, 0.317537604750414, 0.450195189322832, 0.239811667469510, 0.305429446016516, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# x4= [1.0, 0.455178178175743, 0.290585720686775, 0.184484291949937, 0.252933019899052, 0.273972907097112, 0.330307079512898, 0.356468967537745, 0.542486488956359, 0.239811667469510, 0.418311541037243, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# x5= [1.0, 0.301915721341703, 0.270437048408283, 0.454339433915631, 0.252933019899052, 0.537101359844810, 0.180007369566163, 0.317537604750414, 0.411903315713825, 0.239811667469510, 0.182663132775251, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# x6= [1.0, 0.609829383068210, 0.393630018944144, 0.454339433915631, 0.252933019899052, 0.588187426970977, 0.200362300489902, 0.236836061231512, 0.542486488956359, 0.239811667469510, 0.418311541037243, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]
# x7= [1.0, 0.231953305428985, 0.393630018944144, 0.197520521172726, 0.252933019899052, 0.303738591543687, 0.495604254772132, 0.317537604750414, 0.542486488956359, 0.239811667469510, 0.197520521172726, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
# x8= [1.0, 0.185717902351708, 0.263498253576253, 0.342892495132357, 0.198930723087575, 0.388049830059183, 0.200362300489902, 0.317537604750414, 0.153993492408978, 0.239811667469510, 0.390828100183582, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
# x9= [1.0, 0.308839835516894, 0.179112783466585, 0.454339433915631, 0.252933019899052, 0.189925831214831, 0.160123082499971, 0.317537604750414, 0.212539057215358, 0.239811667469510, 0.342892495132357, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]
# x10= [1.0, 0.396446212399178, 1.06243592376559, 0.454339433915631, 0.252933019899052, 0.303738591543687, 0.200362300489902, 0.317537604750414, 0.342892495132357, 0.542486488956359, 0.418311541037243, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]


# tableu = []
# z = [0.0, -1.0, -1.0, -1.0, 0.0, 0.0, 0.0]
# x1 = [1, 1 + 17, 2 * 17, 1, 1.0, 0.0, 0.0]
# x2 = [1, 3 - 2 * 17, 17, 2, 0.0,  1.0, 0.0]
# x3 = [1, 1 + 3 * 17, 4, 17, 0.0, 0.0,  1.0]
#
# tableu.append(z)
# tableu.append(x1)
# tableu.append(x2)
# tableu.append(x3)
# tableu.append(x4)
# tableu.append(x5)
# tableu.append(x6)
# tableu.append(x7)
# tableu.append(x8)
# tableu.append(x9)
# tableu.append(x10)

# tableu = simplex_main(tableu)
#
# print("Fmax = ", tableu[0][0])
# V = 1/tableu[0][0]
# print("V = ", V)
# #
# print("x1= ", V * tableu[1][0])
# print("x2= ", V * tableu[2][0])
# print("x3= ", V * tableu[3][0])
# print("x4= ", V * tableu[4][0])
# print("x5= ", V * tableu[5][0])
# print("x6= ", V * tableu[6][0])
# print("x7= ", V * tableu[7][0])
# print("x8= ", V * tableu[8][0])
# print("x9= ", V * tableu[9][0])
# print("x10= ", V * tableu[10][0])


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
