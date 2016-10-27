__author__ = 'Gebruiker'
#GUI link
#http://www.python-course.eu/tkinter_entry_widgets.php
from tkinter import *

root = Tk()
root.title("Parametric game model solver")
root.geometry("700x500")


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

# rows = []
# for i in range(5):
#     cols = []
#     for j in range(4):
#         e = Entry(root, relief=RIDGE)
#         e.grid(row=i, column=j, sticky=NSEW)
#         e.insert(END, '%d.%d' % (i, j))
#         cols.append(e)
#     rows.append(cols)
#
# print(rows)


var = StringVar(root)
var.set("Cooperative")  # initial value

option = OptionMenu(root, var, "Cooperative game", "Multi parameter game", "One parameter game")
option.pack(padx=10, pady=1, side=LEFT)


def ok():
    print("value is", var.get())
    # root.quit()

button = Button(root, text="OK", command=ok)
button.pack(padx=10, pady=10)


#opens a new window
def create_window():
    window = Toplevel(root)
    window.title("Cooperative game")
    window.geometry("500x500")
    window_label = Label(window, text="Enter transformation level: ")
    window_label.pack()

    rows = []
    for i in range(5):
        cols = []
        for j in range(5):
            e = Entry(window, relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)
            e.insert(END, 0.0)
            cols.append(e)
        rows.append(cols)


b = Button(root, text="Create new window", command=create_window)
b.pack()


root.mainloop()
