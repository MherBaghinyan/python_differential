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

    bnds = ((0, 100), (0, 100))
    if len(x_cons) > 0:
        f_res = minimize(mul_func, [t_value, d_value], args=(-1.0,), constraints=x_cons, method='SLSQP', bounds=bnds, options={'maxiter': 200, 'disp': True, 'ftol': 1.49e-08})
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

    bnds = ((0, 50), (0, 50))
    if len(x_cons) > 0:
        f_res = minimize(mul_func, [0, 0], args=(1.0,), constraints=x_cons, method='SLSQP', bounds=bnds)
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

# x_parametric_array = [-0.00426905456059975*d + 2.3039296165317e-19*t + (d - 10)**5*(-6.97933641841617e-24*t + 6.97933641841617e-23) - 7.25752032803331e-28*(d - 10)**5*(t - 10)**5 - 2.67581619050967e-27*(d - 10)**5*(t - 10)**4 - 1.49441809885068e-26*(d - 10)**5*(t - 10)**3 - 5.20219057113428e-25*(d - 10)**5*(t - 10)**2 - 3.75782427202595e-7*(d - 10)**5 + (d - 10)**4*(4.54949336904165e-23*t - 4.54949336904165e-22) + 5.55358077275592e-27*(d - 10)**4*(t - 10)**5 + 4.44286461820474e-26*(d - 10)**4*(t - 10)**4 + 3.03730381171815e-25*(d - 10)**4*(t - 10)**3 + 2.22304789623626e-24*(d - 10)**4*(t - 10)**2 + 3.77223315590386e-6*(d - 10)**4 + (d - 10)**3*(-2.11758236813575e-22*t + 2.11758236813575e-21) - 3.63507105125842e-26*(d - 10)**3*(t - 10)**5 - 4.65289094561078e-25*(d - 10)**3*(t - 10)**4 - 2.68833699079734e-24*(d - 10)**3*(t - 10)**3 - 1.98523347012727e-23*(d - 10)**3*(t - 10)**2 - 3.86179852522229e-5*(d - 10)**3 + (d - 10)**2*(2.96461531539005e-21*t - 2.96461531539005e-20) + 5.81611368201348e-25*(d - 10)**2*(t - 10)**5 + 4.85968609874904e-24*(d - 10)**2*(t - 10)**4 + 2.06795153138257e-23*(d - 10)**2*(t - 10)**3 + 3.57342024622908e-22*(d - 10)**2*(t - 10)**2 + 0.00040268085576588*(d - 10)**2 + (d - 10)*(-3.55753837846806e-20*t + 3.55753837846806e-19) - 6.61744490042422e-24*(d - 10)*(t - 10)**5 - 4.79764755280756e-23*(d - 10)*(t - 10)**4 - 7.94093388050907e-23*(d - 10)*(t - 10)**3 - 4.12928561786471e-21*(d - 10)*(t - 10)**2 + 4.96308367531817e-23*(t - 10)**5 + 3.4410713482206e-22*(t - 10)**4 + 1.16467030247466e-21*(t - 10)**3 + 1.86347248395946e-20*(t - 10)**2 + 0.0886089129529363, 0, -0.00645564348188255*d + (d - 10)**5*(4.8617962533729e-24*t - 4.8617962533729e-23) - 1.78044296388168e-27*(d - 10)**5*(t - 10)**5 - 1.89913916147379e-26*(d - 10)**5*(t - 10)**4 + 3.79827832294758e-26*(d - 10)**5*(t - 10)**3 - 2.73476039252225e-24*(d - 10)**5*(t - 10)**2 - 2.88177677558184e-8*(d - 10)**5 + (d - 10)**4*(-3.88943700269832e-23*t + 3.88943700269832e-22) + 7.1217718555267e-27*(d - 10)**4*(t - 10)**5 + 1.51931132917903e-25*(d - 10)**4*(t - 10)**4 - 6.07724531671612e-25*(d - 10)**4*(t - 10)**3 + 2.67398793935509e-23*(d - 10)**4*(t - 10)**2 + 1.79130738636857e-6*(d - 10)**4 + (d - 10)**3*(3.11154960215865e-22*t - 3.11154960215865e-21) - 3.79827832294758e-26*(d - 10)**3*(t - 10)**5 - 1.21544906334322e-24*(d - 10)**3*(t - 10)**4 + 1.21544906334322e-23*(d - 10)**3*(t - 10)**3 - 1.94471850134916e-22*(d - 10)**3*(t - 10)**2 - 3.30020064873011e-5*(d - 10)**3 + 4.55793398753709e-25*(d - 10)**2*(t - 10)**5 + 1.21544906334322e-23*(d - 10)**2*(t - 10)**4 - 1.1668311008095e-22*(d - 10)**2*(t - 10)**3 + 1.40019732097139e-21*(d - 10)**2*(t - 10)**2 + 0.000484492005881903*(d - 10)**2 + (d - 10)*(1.99139174538154e-20*t - 1.99139174538154e-19) - 1.21544906334322e-24*(d - 10)*(t - 10)**5 - 3.88943700269832e-23*(d - 10)*(t - 10)**4 + 9.33464880647596e-22*(d - 10)*(t - 10)**3 - 9.95695872690769e-21*(d - 10)*(t - 10)**2 - 9.95695872690769e-21*(t - 10)**3 + 0.14618908788005]
#
# multy_nonlinear_max(x_parametric_array, 10, 10)
