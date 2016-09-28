__author__ = 'Gebruiker'

from tkinter import *

root = Tk()

theLabel = Label(root, text="Game theory software")
theLabel.pack()


def evaluate(event):
    data = e.get()
    answer.configure(text="Answer is= " + str(eval(data)))


e = Entry(root)
e.bind('<Return>', evaluate)
e.pack()
answer = Label(root)
answer.pack()


root.mainloop()
