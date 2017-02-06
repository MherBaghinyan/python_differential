# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from tkinter import *
from transformation_util import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


def graph_window(root, item):
    graph_root = Toplevel(root)
    graph_root.title("game model graph")
    graph_root.geometry("600x600")

    f = Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)

    point_vec = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]

    func_vec = [0 for x in range(len(point_vec))]

    for i in range(len(point_vec)):
        func_vec[i] = item.evalf(subs={t: point_vec[i]})

    a.plot(point_vec,
           func_vec)

    canvas = FigureCanvasTkAgg(f, graph_root)
    canvas.show()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    toolbar = NavigationToolbar2TkAgg(canvas, graph_root)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    graph_root.mainloop()
