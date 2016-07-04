from tkinter import *

root = Tk()
root.geometry("500x500")

w = Label(root, text="Insert the payoff matrix")
w.pack()


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


button = Button(root, text='create the parametric linear programming  model', width=50, command=root.destroy)
button.pack()

root.mainloop()