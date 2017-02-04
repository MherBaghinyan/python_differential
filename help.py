# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from tkinter import *


def help_window(root):
    help_root = Toplevel(root)
    help_root.title("Applied package guide")
    help_root.geometry("800x600")

    # top level bar
    Label(help_root, text=' Guide to use software ').grid(row=0, column=0, padx=10, pady=10)
    Label(help_root, text=' ---------------------------------------- ').grid(row=1, column=0, padx=10, pady=10)
    Label(help_root, text=' All the parametric expressions should be entered '
                          'to the system by strictly following this rules!!! ').grid(row=2, column=0, padx=10, pady=10)

    help_root.mainloop()
