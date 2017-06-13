# https://docs.scipy.org/doc/scipy-0.18.1/reference/tutorial/optimize.html#constrained-minimization-of-multivariate-scalar-functions-minimize
from scipy.optimize import minimize
from project_files.services.transformation_util import *
import math


# def func(x, sign=1.0):
#     """ Objective function """
#     return sign*(2*x[0]*x[1] + 2*x[0] - x[0]**2 - 2*x[1]**2)
#
#
# cons = ({'type': 'eq',
#          'fun' : lambda x: np.array([x[0]**3 - x[1]])},
#         {'type': 'ineq',
#          'fun' : lambda x: np.array([x[1] - 1])})
#
#
# res = minimize(func, [0.0, 0.0], args=(-1.0,),
#                constraints=cons, method='SLSQP', options={'disp': True})
#
# print(res.x)


def func_deriv(x, sign=1.0):
    """ Derivative of objective function """
    return np.array([sign * 1])


def func_test(x, sign=1.0):
        """ Objective function """
        return sign * x[0]


def test_max_optimize():

    cons = [{'type': 'ineq', 'fun': lambda x: np.array([3.32929*x[0]**2 + 5.0]),
             'jac': lambda x: np.array([3.32929*2*x[0]])}]

# 'jac': lambda x: np.array([diff(x_b_array[i], t, 1) if is_number(diff(x_b_array[i], t, 1)) else diff(x_b_array[i], t, 1).evalf(subs={t: x[0]})])

    res = minimize(func_test, 1.0, args=(-1.0,), jac=func_deriv, constraints=cons, method='SLSQP', options={'disp': True})
    print(res.x)
    print(res.x[0])


def test_min_optimize():

    cons = [{'type': 'ineq', 'fun': lambda x: np.array([3.32929*x[0]**2 + 5.0]),
             'jac': lambda x: np.array([3.32929*2*x[0]])}]

    res = minimize(func_test, 1.0, args=(1.0,), jac=func_deriv, constraints=cons, method='SLSQP', options={'disp': True})
    print(res.x)
    print(res.x[0])


# test_max_optimize()
# print("============ min ================")
# test_min_optimize()


# ================= mul ======================

def mul_func(x, sign=1.0):
    """ Objective function """
    return sign * (x[0] + x[1])


def multy_nonlinear_max():

    x_array = [2*d + t + 5, d + 1]

    x_cons = []
    solo_item = 0
    for i in range(len(x_array)):
        if not is_number(x_array[i]):
            solo_item = x_array[i]
            x_cons.append({'type': 'ineq', 'fun': lambda x: np.array([x_array[i].evalf(subs={t: x[0], d: x[1]})])})

    if len(x_cons) == 1:
        x_cons = [{'type': 'ineq', 'fun': lambda x: np.array([solo_item.evalf(subs={t: x[0], d: x[1]})])}]

    if len(x_cons) > 0:
        f_res = minimize(mul_func, [0, 0], args=(-1.0,), constraints=x_cons, method='SLSQP')
        print(f_res.x)
        print("t = ", f_res.x[0] if f_res.x[0] > 0 else math.nan)
        print("d = ", f_res.x[1] if f_res.x[1] > 0 else math.nan)
        return f_res.x[0]

    return math.nan


# print(multy_nonlinear_max())
