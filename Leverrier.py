from sympy import *
import numpy as np

t = Symbol('t')
S_matrix = [[1, 2*t, 1/t], [-t, 2, 0], [t, t - 1, t*(t - 1)]]

print(S_matrix)

def differential(matrix, level):
    "returns a differential of given matrix"
    t = Symbol('t')
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print(diff(matrix[i][j], t, level))
    print(diff(sin(t), t))


def p_items(matrix, index):
    count = len(S_matrix)
    for k in range(0, index):
        (1 / k) * (differential(S_matrix, k))



def calculateLeverrier(start, end):
    count = len(S_matrix)
    p_item = [0 for x in range(len(S_matrix))]
    for n in range(start, end):
        p_items(S_matrix, n)
        print(p_item[n])
    return p_item

print(calculateLeverrier(1, len(S_matrix)))
