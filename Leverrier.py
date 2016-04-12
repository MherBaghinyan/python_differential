from sympy import *
import numpy as np

t = Symbol('t')
matrix = [[1, 2*t, 1/t], [-t, 2, 0], [t, t - 1, t*(t - 1)]]

print(matrix)

def differential(matrix, level):
    "returns a differential of given matrix"
    t = Symbol('t')
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print(diff(matrix[i][j], t, level))
    print(diff(sin(t), t))


x = Symbol('x')
y = Symbol('y')

print(x + x + x)


differential(matrix, 1)

print(np.dot(matrix, matrix))
