__author__ = 'Gebruiker'
#GUI link
#http://www.python-course.eu/tkinter_entry_widgets.php
from tkinter import *

root = Tk()
root.title("Parametric game model solver")
root.geometry("700x700")


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
    # window_label = Label(window, text="Enter transformation level: ")
    # window_label.pack()

    Label(window, text='N=').grid(row=0, column=0)
    n = Entry(window, relief=RIDGE)
    n.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5)
    n.insert(END, 2)


b = Button(root, text="Create new window", command=create_window)
b.pack()


fields = 'm =', 'n ='


def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))


def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries


matrix_sizes = makeform(root, fields)
root.bind('<Return>', (lambda event, e=matrix_sizes: fetch(e)))
b1 = Button(root, text='Show',
      command=(lambda e=matrix_sizes: fetch(e)))
b1.pack(side=LEFT, padx=5, pady=5)
b2 = Button(root, text='Quit', command=root.quit)
b2.pack(side=LEFT, padx=5, pady=5)


root.mainloop()
