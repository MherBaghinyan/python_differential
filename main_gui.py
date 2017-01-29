#http://www.python-course.eu/tkinter_entry_widgets.php
from tkinter import *
from cooperative_gui import *

root = Tk()
root.title("Parametric game model solver")
root.geometry("400x400")

n_value = 2
m_value = 2

Label(root, text='Enter payoff matrix metrics').grid(row=1, column=0)

Label(root, text='N=').grid(row=2, column=0)
n = Entry(root, relief=RIDGE)
n.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)
n.insert(END, n_value)
Label(root, text='M=').grid(row=3, column=0)
m = Entry(root, relief=RIDGE)
m.grid(row=3, column=1, sticky=NSEW, padx=5, pady=5)
m.insert(END, m_value)


def create_cooperative_window():
    cooperative_window(root, n_value, m_value)


def create_one_parameter_window():
    print()


def create_multi_parameter_window():
    print()


def create_help_window():
    print()

Button(root, text='Cooperative game', command=create_cooperative_window).grid()
Button(root, text='One parameter game', command=create_one_parameter_window).grid()
Button(root, text='Multi parameter game', command=create_multi_parameter_window).grid()
Button(root, text='Help', command=create_help_window).grid()

root.mainloop()
