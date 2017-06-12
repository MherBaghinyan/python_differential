# https://docs.scipy.org/doc/scipy-0.18.1/reference/tutorial/optimize.html#constrained-minimization-of-multivariate-scalar-functions-minimize
from scipy.optimize import minimize
from project_files.services.transformation_util import *
import math


def func(x, sign=1.0):
    """ Objective function """
    return sign*(2*x[0]*x[1] + 2*x[0] - x[0]**2 - 2*x[1]**2)


cons = ({'type': 'eq',
         'fun' : lambda x: np.array([x[0]**3 - x[1]])},
        {'type': 'ineq',
         'fun' : lambda x: np.array([x[1] - 1])})


res = minimize(func, [0.0, 0.0], args=(-1.0,),
               constraints=cons, method='SLSQP', options={'disp': True})

print(res.x)
