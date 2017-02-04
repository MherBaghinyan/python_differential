# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from tkinter import *
from Simplex_Parametric_Right import *


def report_window(root, matrix, vector, k_value):
    report_root = Toplevel(root)
    report_root.title("game model report")
    report_root.geometry("1200x800")
    approx_centers = [0.0, 0.5, 1.5, 7.0]
    # top level bar
    Label(report_root, text=' K ').grid(row=0, column=0)
    Label(report_root, text=' t = ' + str(approx_centers[0]) + ' ').grid(row=0, column=1)
    Label(report_root, text=' t = ' + str(approx_centers[1]) + ' ').grid(row=0, column=2)
    Label(report_root, text=' t = ' + str(approx_centers[2]) + ' ').grid(row=0, column=3)
    Label(report_root, text=' t = ' + str(approx_centers[3]) + ' ').grid(row=0, column=4)

    # left side bar
    for k in range(k_value + 1):
        value = " V( " + str(k) + " ) "
        Label(report_root, text=value).grid(row=k + 1, column=0)

    Label(report_root, text=' V( t ) ').grid(row=k + 1, column=0)
    Label(report_root, text=' R1( t ) ').grid(row=k + 2, column=0)
    Label(report_root, text=' R2( t ) ').grid(row=k + 3, column=0)
    Label(report_root, text=' R3( t ) ').grid(row=k + 4, column=0)

    length = len(approx_centers)
    for app in range(length):
        parametric_array = [0 for x in range(len(vector))]
        x_b_image_matrix = parametric_simplex_solution(matrix, vector, k_value, approx_centers[app], parametric_array)

        for k in range(0, k_value + 1):
            s_item = 0
            for j in range(0, len(vector)):
                s_item += x_b_image_matrix[k][j]
            Label(report_root, text=str(s_item)).grid(row=k + 1, column=app + 1)

        Label(report_root, text=str(1/sum(parametric_array))).grid(row=k + 1, column=app + 1)
        Label(report_root, text=str(parametric_array[0])).grid(row=k + 2, column=app + 1)
        Label(report_root, text=str(parametric_array[0])).grid(row=k + 3, column=app + 1)
        Label(report_root, text=str(parametric_array[0])).grid(row=k + 4, column=app + 1)

    report_root.mainloop()
