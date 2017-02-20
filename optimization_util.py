# https://docs.scipy.org/doc/scipy-0.18.1/reference/tutorial/optimize.html#constrained-minimization-of-multivariate-scalar-functions-minimize
import math
import numpy as np
from scipy.optimize import minimize
from transformation_util import *


def func(x, sign=1.0):
        """ Objective function """
        return sign * x[0]


def nonlinear_optimality(image_matrixes, k_value, vector_len, t_value):

    x_b_array = [0 for x in range(vector_len)]
    columns = len(image_matrixes[0][0])
    f_array = [0 for x in range(len(image_matrixes[0][0]) - 1)]

    for k in range(0, k_value + 1):
        image_matrix = image_matrixes[k]
        rows = len(image_matrix)
        for j in range(1, rows):
            s_item = image_matrix[j][0] * ((t-t_value)**k)
            x_b_array[j - 1] += s_item
        for i in range(1, columns):
            f_item = image_matrix[0][i] * ((t-t_value)**k)
            f_array[i - 1] += f_item

    x_b_cons = []
    for i in range(len(x_b_array)):
        x_b_cons.append({'type': 'ineq', 'fun': lambda x: np.array([x_b_array[i].evalf(subs={t: x[0]})])})

    f_cons = []
    for i in range(len(f_array)):
        if not is_number(f_array[i]):
            f_cons.append({'type': 'ineq', 'fun': lambda x: np.array([f_array[i].evalf(subs={t: x[0]})])})

    # cons = [{'type': 'ineq', 'fun': lambda x: np.array([-(2*x - 10)])},
    #         {'type': 'ineq', 'fun': lambda x: np.array([-(-x - 30)])},
    #         {'type': 'ineq', 'fun': lambda x: np.array([-(7*x - 30)])}]

    if len(f_cons) > 0:
        f_res = minimize(func, 0.0, args=(-1.0,), constraints=f_cons, method='SLSQP')

    x_b_res = minimize(func, 0.0, args=(-1.0,), constraints=x_b_cons, method='SLSQP')

    print(x_b_res.x[0])
    if len(f_cons) > 0 and (t_value < x_b_res.x[0] < x_b_res.x[0]):
        return f_res.x[0]

    return x_b_res.x[0]


def lamb(x):
    return np.array([-(2*x - 10)])


def test_optimize():

    cons = [{'type': 'ineq', 'fun': lambda x: lamb(x[0])},
            {'type': 'ineq', 'fun': lambda x: np.array([-(-x[0] - 30)])},
            {'type': 'ineq', 'fun': lambda x: np.array([-(7*x[0] - 30)])}]

    res = minimize(func, [0.0], args=(-1.0,), constraints=cons, method='SLSQP')



# test_optimize()
