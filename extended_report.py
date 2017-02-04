# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from tkinter import *


def report_window(root, matrix, vector, k_value):
    report_root = Toplevel(root)
    report_root.title("game model report")
    report_root.geometry("800x600")

# top level bar
    Label(report_root, text=' K ').grid(row=0, column=0)
    Label(report_root, text=' t = 0 ').grid(row=0, column=1)
    Label(report_root, text=' t = 0.5 ').grid(row=0, column=2)
    Label(report_root, text=' t = 1.5 ').grid(row=0, column=3)
    Label(report_root, text=' t = 7 ').grid(row=0, column=4)

# left side bar
    for k in range(k_value + 1):
        value = " V( " + str(k) +" ) "
        Label(report_root, text=value).grid(row=1, column=0)

    report_root.mainloop()
