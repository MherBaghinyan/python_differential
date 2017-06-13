# https://docs.scipy.org/doc/scipy-0.18.1/reference/tutorial/optimize.html#constrained-minimization-of-multivariate-scalar-functions-minimize
from scipy.optimize import minimize
from project_files.services.transformation_util import *
import math


def func(x, sign=1.0):
        """ Objective function """
        return sign * x[0]


def mul_func(x, sign=1.0):
    """ Objective function """
    return sign * (x[0] + x[1])


def multy_nonlinear_max(x_parametric_array, d_value, t_value):

    x_array = x_parametric_array

    x_cons = []
    solo_item = 0
    print(x_array)
    for i in range(len(x_array)):
        if not is_number(x_array[i]):
            solo_item = x_array[i]
            x_cons.append({'type': 'ineq', 'fun': lambda x: np.array([x_array[i].evalf(subs={t: x[0], d: x[1]})])})

    if len(x_cons) == 1:
        x_cons = [{'type': 'ineq', 'fun': lambda x: np.array([solo_item.evalf(subs={t: x[0], d: x[1]})])}]

    if len(x_cons) > 0:
        f_res = minimize(mul_func, [t_value, d_value], args=(-1.0,), constraints=x_cons, method='SLSQP')
        print(f_res.x)
        print("t = ", f_res.x[0] if f_res.x[0] > 0 else math.nan)
        print("d = ", f_res.x[1] if f_res.x[1] > 0 else math.nan)
        return f_res.x[0]

    return math.nan


def multy_nonlinear_min(x_parametric_array, d_value, t_value):

    x_array = x_parametric_array

    x_cons = []
    solo_item = 0
    print(x_array)
    for i in range(len(x_array)):
        if not is_number(x_array[i]):
            solo_item = x_array[i]
            x_cons.append({'type': 'ineq', 'fun': lambda x: np.array([x_array[i].evalf(subs={t: x[0], d: x[1]})])})

    if len(x_cons) == 1:
        x_cons = [{'type': 'ineq', 'fun': lambda x: np.array([solo_item.evalf(subs={t: x[0], d: x[1]})])}]

    if len(x_cons) > 0:
        f_res = minimize(mul_func, [t_value, d_value], args=(1.0,), constraints=x_cons, method='SLSQP')
        print(f_res.x)
        print("t = ", f_res.x[0] if f_res.x[0] > 0 else math.nan)
        print("d = ", f_res.x[1] if f_res.x[1] > 0 else math.nan)
        return f_res.x[0]

    return math.nan


def z_nonlinear_optimality(image_matrixes, x_b_image_matrix, k_value, vector_len, t_value):

    columns = len(image_matrixes[0][0])
    f_array = [0 for x in range(len(image_matrixes[0][0]) - 1)]

    for k in range(0, k_value + 1):
        image_matrix = image_matrixes[k]
        for i in range(1, columns):
            f_item = image_matrix[0][i] * ((t-t_value)**k)
            f_array[i - 1] += f_item

    print("f_array = ", f_array)
    f_cons = []
    solo_item = 0
    for i in range(len(f_array)):
        if not is_number(f_array[i]):
            solo_item = f_array[i]
            f_cons.append({'type': 'ineq', 'fun': lambda x: np.array([f_array[i].evalf(subs={t: x[0]})])})

    if len(f_cons) == 1:
        f_cons = [{'type': 'ineq', 'fun': lambda x: np.array([solo_item.evalf(subs={t: x[0]})])}]

    if len(f_cons) > 0:
        f_res = minimize(func, 0.0, args=(-1.0,), constraints=f_cons, method='SLSQP')
        print(f_res.x)
        return f_res.x[0]

    return math.nan


def x_b_max_optimality(image_matrixes, k_value, vector_len, t_value, basis_vector, bound_):

    x_b_array = [0 for x in range(vector_len)]

    for i in range(0, k_value + 1):
        image_matrix = image_matrixes[i]
        for j in range(0, vector_len):
            x_b_array[j] += image_matrix[j + 1][0] * ((t-t_value)**i)

    for b in range(len(basis_vector)):
        if basis_vector[b] > len(basis_vector):
            x_b_array[b] = 0
            basis_vector[b] = 1

    print("x_b = ", x_b_array)
    x_b_cons = []
    # x_b_array = list(set(x_b_array))
    for i in range(len(x_b_array)):
        if not is_number(x_b_array[i]):
            x_b_cons.append({'type': 'ineq', 'fun': lambda x: np.array([x_b_array[i].evalf(subs={t: x[0]})])})

    if len(x_b_cons) > 0:
        res = minimize(func, 0.0, args=(-1.0,), constraints=x_b_cons, method='SLSQP')
        if 0 < bound_ < res.x[0]:
            print(bound_)
            return bound_
        print(res.x)
        return res.x[0]

    return math.nan


def x_b_min_optimality(image_matrixes, k_value, vector_len, t_value, basis_vector):

    x_b_array = [0 for x in range(vector_len)]

    for i in range(0, k_value + 1):
        image_matrix = image_matrixes[i]
        for j in range(0, vector_len):
            x_b_array[j] += image_matrix[j + 1][0] * ((t-t_value)**i)

    for b in range(len(basis_vector)):
        if basis_vector[b] > len(basis_vector):
            x_b_array[b] = 0
            basis_vector[b] = 1

    print("x_b = ", x_b_array)
    x_b_cons = []
    for i in range(len(x_b_array)):
        if not is_number(x_b_array[i]):
            x_b_cons.append({'type': 'ineq', 'fun': lambda x: np.array([x_b_array[i].evalf(subs={t: x[0]})])})

    if len(x_b_cons) > 0:
        res = minimize(func, 0.0, args=(1.0,), constraints=x_b_cons, method='SLSQP')
        print(res.x if res.x[0] > 0 else math.nan)
        return res.x[0] if res.x[0] > 0 else math.nan

    return math.nan

