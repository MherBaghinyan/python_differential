__author__ = 'Gebruiker'
#GUI link
#http://www.python-course.eu/tkinter_layout_management.php
from tkinter import *

root = Tk()
root.title("Parametric game model solver")
root.geometry("500x500")


def evaluate(event):
    data = transformationEntry.get()
    transformationLabel.configure(text="K= " + str(eval(data)))


matrixLabel = Label(root, text="Enter transformation level: ")
matrixLabel.pack(padx=10, pady=1, side=LEFT)
transformationEntry = Entry(root)
transformationEntry.bind('<Return>', evaluate)
transformationEntry.pack(padx=10, pady=1, side=LEFT)
transformationLabel = Label(root)
transformationLabel.pack(padx=10)


var = StringVar(root)
var.set("Cooperative")  # initial value

option = OptionMenu(root, var, "Cooperative", "Multi parameter game", "One parameter game")
option.pack(padx=10, pady=1, side=LEFT)


def ok():
    print("value is", var.get())
    # root.quit()

button = Button(root, text="OK", command=ok)
button.pack(padx=10, pady=10)


#opens a new window
def create_window():
    window = Toplevel(root)


b = Button(root, text="Create new window", command=create_window)
b.pack()


root.mainloop()
