# https://docs.scipy.org/doc/scipy-0.18.1/reference/tutorial/optimize.html#constrained-minimization-of-multivariate-scalar-functions-minimize
from scipy.optimize import minimize
from project_files.services.transformation_util import *
import math


def multy_nonlinear_max(x_parametric_array, d_value, t_value):

    x_array = x_parametric_array

    d_start = d_value
    t_start = t_value

    d_end = 50
    t_end = 50

    d_step = 5
    t_step = 1

    d_optimal = d_start
    t_optimal = t_start

    # d_bound = bounds[0]
    # t_bound = bounds[1]

    print(x_array)

    bool = false

    i = d_start
    j = t_start

    while i <= d_end:
        # if k1 > d_bound:
        #     break
        while j < t_end:
            # if k2 > t_bound:
            #     break
            for k in range(len(x_array)):
                if not is_number(x_array[k]):
                    bool = -x_array[k].evalf(subs={t: t_optimal + t_step, d: d_optimal + d_step}) <= 0
                    if bool:
                        t_optimal += t_step
                    else:
                        if j == t_start:
                            if d_step == 5:
                                d_step = 1
                            d_step /= 10
                            if d_step == 0.0001:
                                print("d_optimal = ", d_optimal)
                                # print("t_optimal = ", t_optimal)
                                return [d_optimal, t_optimal]
                            break
                        t_step /= 10
                        if t_step == 0.0001:
                            # print([d_optimal, t_optimal])
                            print("d_optimal = ", d_optimal)
                            # print("t_optimal = ", t_optimal)
                            return [d_optimal, t_optimal]
            j += t_step
        j = t_start
        t_optimal = t_start
        i += d_step
        if bool:
            d_optimal += d_step
        else:
            d_step /= 10
            if d_step == 0.0001:
                # print([d_optimal, t_optimal])
                print("d_optimal = ", d_optimal)
                # print("t_optimal = ", t_optimal)
                return [d_optimal, t_optimal]
        bool = false

    print("d_optimal = ", d_end)
    return [d_end, t_end]


def multy_reverse_nonlinear_max(x_parametric_array, d_value, t_value):

    x_array = x_parametric_array

    d_start = d_value
    t_start = t_value

    d_end = 50
    t_end = 50

    d_step = 1
    t_step = 1

    d_optimal = d_start
    t_optimal = t_start

    print(x_array)
    for k1 in range(t_start, t_end + 1, t_step):
        for k2 in range(d_start, d_end + 1, d_step):
            for i in range(len(x_array)):
                if not is_number(x_array[i]):
                    bool = -x_array[i].evalf(subs={t: t_optimal + t_step, d: d_optimal + d_step}) <= 0
                    if bool:
                        t_optimal += t_step
                        d_optimal += d_step
                    else:
                        d_step /= 10
                        t_step /= 10
                        if d_step == 0.0001 and t_step == 0.0001:
                            print([d_optimal, t_optimal])
                            print("d_optimal = ", d_optimal)
                            print("t_optimal = ", t_optimal)
                            return [d_optimal, t_optimal]

    return math.nan


def solo_nonlinear_max(x_parametric_array, t_value, d_optimal):

    x_array = x_parametric_array

    t_start = t_value

    t_end = 50

    t_step = 1

    t_optimal = t_start

    for k2 in range(t_start, t_end + 1, t_step):
        for i in range(len(x_array)):
            if not is_number(x_array[i]):
                bool = -x_array[i].evalf(subs={t: t_optimal + t_step, d: d_optimal}) <= 0
                if t_optimal > t_end:
                    print(t_end)
                    return t_end
                if bool:
                    t_optimal += t_step
                else:
                    t_step /= 10
                    if t_step == 0.0001:
                        print("t_optimal = ", t_optimal)
                        return t_optimal

    print("t_optimal = ", t_optimal)
    return t_optimal


# k1,k2=5
# x_parametric_array = [-0.00426905456059975*d + 2.3039296165317e-19*t + (d - 10)*(-3.55753837846806e-20*t + 3.55753837846806e-19) + 0.0886089129529363, 0, -0.00645564348188255*d + (d - 10)*(1.99139174538154e-20*t - 1.99139174538154e-19) + 0.14618908788005]


# naver
x_parametric_array = [0, -4.13602670802749*d - 6.69275490563015e-8*t + (d - 0.5)**2*(2.95343527662159e-12*t - 7.38358819155397e-11) - 2.95342808487512e-13*(d - 0.5)**2*(t - 25)**2 + 8.27205676240782*(d - 0.5)**2 + (d - 0.5)*(-1.33854113631795e-7*t + 3.34635284079487e-6) + 8.03118774920441e-9*(d - 0.5)*(t - 25)**2 + 4.01564309856996e-9*(t - 25)**2 + 4.13603005440494, 0, -20.9713842362948*d - 2.93381214789896e-7*t + (d - 0.5)**2*(8.37794749763616e-13*t - 2.09448687440904e-11) - 8.37797340853945e-14*(d - 0.5)**2*(t - 25)**2 + 41.9427831416434*(d - 0.5)**2 + (d - 0.5)*(-5.86762150315607e-7*t + 1.46690537578902e-5) + 3.52057122630419e-8*(d - 0.5)*(t - 25)**2 + 1.7602870094752e-8*(t - 25)**2 + 20.9713989053555, 0, 0, -4.61297459700219*d - 2.00687920573667e-7*t + (d - 0.5)**2*(3.42259211421014e-12*t - 8.55648028552536e-11) - 3.42258399882404e-13*(d - 0.5)**2*(t - 25)**2 + 9.2259592283719*(d - 0.5)**2 + (d - 0.5)*(-4.01374700280664e-7*t + 1.00343675070166e-5) + 2.4082413564998e-8*(d - 0.5)*(t - 25)**2 + 1.20412638257531e-8*(t - 25)**2 + 4.61298463139822, 0, 0, -0.990292563137412*d - 1.24372554828432e-7*t + (d - 0.5)**2*(-7.63414304535253e-13*t + 1.90853576133813e-11) + 7.63412398422309e-14*(d - 0.5)**2*(t - 25)**2 + 1.98059134490893*(d - 0.5)**2 + (d - 0.5)*(-2.48745364128979e-7*t + 6.21863410322448e-6) + 1.49247371160224e-8*(d - 0.5)*(t - 25)**2 + 7.46235583442698e-9*(t - 25)**2 + 0.990298781765151]

# d_bound = 2.5
# t_bound = 100
#
# bounds = [d_bound, t_bound]

# d_value = 0.5
# t_value = 25
# optimal = multy_nonlinear_max(x_parametric_array, d_value, t_value)
#
# solo_nonlinear_max(x_parametric_array, t_value, optimal[0] - 1)
