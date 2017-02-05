# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
from tkinter import *
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
    a.plot([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6],
           [139.9252434, 141.7788191, 143.6821622, 145.6373046, 147.6463898, 149.7116815, 151.835572, 154.0205909, 156.269416, 158.5848834, 160.97, 163.4279565, 165.9621412, 168.5761562, 171.2738338, 174.0592561, 176.9367745
])

    canvas = FigureCanvasTkAgg(f, graph_root)
    canvas.show()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    toolbar = NavigationToolbar2TkAgg(canvas, graph_root)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    graph_root.mainloop()
