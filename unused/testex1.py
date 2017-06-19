import numpy as np
from scipy.optimize import minimize

""" If we have to maximize, we can minimize the negative of the objective funcion """

def func(x, sign=1.0):
    """ Objective function """
    val = -(x[0]+x[1])
    return val


def func_deriv(x, sign=1.0):
    """ Derivative of objective function """
    dfdx0 = -1
    dfdx1 = -1
    return np.array([ dfdx0, dfdx1 ])


cons = ({'type': 'ineq',
         'fun' : lambda x: -(0.00426905456059975*x[0] - 2.3039296165317e-19*x[1] - (x[0] - 10)*(-3.55753837846806e-20*x[1] + 3.55753837846806e-19) - 0.0886089129529363)},
        {'type': 'ineq',
         'fun' : lambda x: -(0.00645564348188255*x[0] - (x[0] - 10)*(1.99139174538154e-20*x[1] - 1.99139174538154e-19) - 0.14618908788005)})

bnds = ((0, None), (0, None))

guess = [10.0, 0.0]

# res = minimize(func, guess, jac=func_deriv, bounds = bnds, constraints = cons,
#                method='SLSQP', options={'disp': True})
#
#
# print(res.x)
