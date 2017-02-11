# https://docs.scipy.org/doc/scipy-0.18.1/reference/tutorial/optimize.html#constrained-minimization-of-multivariate-scalar-functions-minimize
import math
import numpy as np
from scipy.optimize import minimize


def func(x, sign=1.0):
        """ Objective function """
        return sign*(x[0])


def nonlinear_optimality():

    cons = ({'type': 'ineq', 'fun': lambda x: np.array([-(2*x[0] - 10)])},
            {'type': 'ineq', 'fun': lambda x: np.array([-(-x[0] - 30)])},
            {'type': 'ineq', 'fun': lambda x: np.array([-(7*x[0] - 30)])})

    res = minimize(func, [0.0], args=(-1.0,), constraints=cons, method='SLSQP')

    print(res.x)
    print(math.isnan(float(res.x)))


nonlinear_optimality()
