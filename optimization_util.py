# https://docs.scipy.org/doc/scipy-0.18.1/reference/tutorial/optimize.html#constrained-minimization-of-multivariate-scalar-functions-minimize
import math
import numpy as np
from scipy.optimize import minimize
from transformation_util import *


def func(x, sign=1.0):
        """ Objective function """
        return sign * x[0]


def nonlinear_optimality(image_matrixes, k, vector_len, t_value):

    parametric_array = [0 for x in range(vector_len)]

    for i in range(0, k + 1):
        image_matrix = image_matrixes[i]
        rows = len(image_matrix)
        for j in range(1, rows):
            s_item = image_matrix[j][0] * ((t-t_value)**i)
            parametric_array[j - 1] += s_item

    cons = []
    for i in range(len(parametric_array)):
        cons.append({'type': 'ineq', 'fun': lambda x: np.array([parametric_array[i].evalf(subs={t: x[0]})])})

    # cons = [{'type': 'ineq', 'fun': lambda x: np.array([-(2*x - 10)])},
    #         {'type': 'ineq', 'fun': lambda x: np.array([-(-x - 30)])},
    #         {'type': 'ineq', 'fun': lambda x: np.array([-(7*x - 30)])}]

    res = minimize(func, 0.0, args=(-1.0,), constraints=cons, method='SLSQP')

    print(res.x)
    print(math.isnan(float(res.x)))
    return res.x[0]


def lamb(x):
    return np.array([-(2*x - 10)])


def test_optimize():

    cons = [{'type': 'ineq', 'fun': lambda x: lamb(x[0])},
            {'type': 'ineq', 'fun': lambda x: np.array([-(-x[0] - 30)])},
            {'type': 'ineq', 'fun': lambda x: np.array([-(7*x[0] - 30)])}]

    res = minimize(func, [0.0], args=(-1.0,), constraints=cons, method='SLSQP')

    print(res.x)
    print(math.isnan(float(res.x)))


# test_optimize()
