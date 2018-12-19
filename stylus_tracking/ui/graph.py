import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


class Graph:
    def __init__(self, master, width, height):
        plt.xkcd()
        fig = Figure(figsize=(width, height))
        self.graph_canvas = FigureCanvasTkAgg(fig, master=master)
        self.ax = Axes3D(fig)
        self.ax.mouse_init()
        self.graph_canvas.get_tk_widget().grid(row=1, column=2)

    def update(self, x, y, z):
        self.ax.clear()
        self.ax.scatter(x, y, z)
        self.graph_canvas.draw()
