import matplotlib.pyplot as plt

def vis():
    import Astar

def vis1():
    import Dijkstra


def vis2():
    import BFS

def vis3():
    import Hillclimbing


def vis4():
    import DFS


def vis5():
    import Beam



def vis6():
    from Astar import n as Astar_cells_path
    from Astar import m as Astar_cells_vis
    from Beam import n as Beam_cells_path
    from Beam import m as Beam_cells_vis
    from BFS import n as BFS_cells_path
    from BFS import m as BFS_cells_vis
    from DFS import n as DFS_cells_path
    from DFS import m as DFS_cells_vis
    from Hillclimbing import n as Hill_cells_path
    from Hillclimbing import m as Hill_cells_vis
    from Dijkstra import n as Dijsktra_cells_path
    from Dijsktra import m as Dijkstra_cells_vis
    cells_visited_by_Dijkstra_search = Dijkstra_cells_vis
    cells_taken_in_path_by_Dijkstra_search = Dijsktra_cells_path
    cells_visited_by_Hill_climbing_search = Hill_cells_vis
    cells_taken_in_path_by_Hill_climbing_search= Hill_cells_path
    cells_visited_by_DFS_search = DFS_cells_vis
    cells_taken_in_path_by_DFS_search = DFS_cells_path
    cells_visited_by_A_star_search = Astar_cells_vis
    cells_taken_in_path_by_A_star_search = Astar_cells_path
    cells_taken_in_path_by_Beam_search = Beam_cells_path
    cells_visited_by_Beam_search = Beam_cells_vis
    cells_visited_by_BFS_search= BFS_cells_vis
    cells_taken_in_path_by_BFS_search = BFS_cells_path
    xxx = [cells_taken_in_path_by_A_star_search / cells_visited_by_A_star_search,
           cells_taken_in_path_by_Dijkstra_search / cells_visited_by_Dijkstra_search,
           cells_taken_in_path_by_BFS_search / cells_visited_by_BFS_search,
           cells_taken_in_path_by_Hill_climbing_search / cells_visited_by_Hill_climbing_search,
           cells_taken_in_path_by_DFS_search / cells_visited_by_DFS_search,
           cells_taken_in_path_by_Beam_search / cells_visited_by_Beam_search]
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    a = xxx[0] / 8
    a_star_x = x
    a_star_y = []
    beam_x = x
    beam_y = []
    w = xxx[5] / 8
    bfs_x = x
    bfs_y = []
    g = xxx[2] / 8
    dfs_x = x
    dfs_y = []
    v = xxx[4] / 8
    hill_x = x
    hill_y = []
    o = xxx[3] / 8
    dij_x = x
    dij_y = []
    s = xxx[1] / 8
    for i in range(1, 9):
        a_star_y.append(i * a * 2)
        beam_y.append(i * w * 2)
        bfs_y.append(i * g * 2)
        dfs_y.append(i * v * 2)
        hill_y.append(i * o * 2)
        dij_y.append(i * s * 2)
    axis = plt.gca()
    axis.set_xlim([0, 9])
    axis.set_ylim([0, 1])
    plt.ylabel('Total Cells in Path/Total Cells Visited')
    plt.xlabel('Intervals')
    plt.plot(a_star_x, a_star_y, color='red')
    plt.plot(beam_x, beam_y, color='pink')
    plt.plot(bfs_x, bfs_y, color='green')
    plt.plot(dfs_x, dfs_y, color='black')
    plt.plot(hill_x, hill_y, color='yellow')
    plt.plot(dij_x, dij_y, color='purple')
    plt.legend(['A Star Search', 'Beam Search', 'Breadth First Search', 'Depth first Search', 'Hill Climbing Search',
                'Dijkstra Search'], loc='upper left')
    plt.show()

def vis7():
    import Analysis

import tkinter as tk
from tkinter import font  as tkfont



class Algorithms(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Visualization, AStar, Dijkstra, BFS, Hill, DFS, Beam, Analysis):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Visualization")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class Visualization(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the VisualSearch", font=controller.title_font)
        label1 = tk.Label(self, text="Press the Buttons to Visualize the respective Search Algos: ", font=("Helvetica", 10))
        label.pack(side="top", fill="x", pady=10)
        label1.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="A Star Search",
                            command=lambda: controller.show_frame("AStar"))
        button2 = tk.Button(self, text="Dijkstra Search",
                            command=lambda: controller.show_frame("Dijkstra"))
        button3 = tk.Button(self, text="Breadth First Search",
                            command=lambda: controller.show_frame("BFS"))
        button4 = tk.Button(self,text="Hill Climbing Search",
                            command=lambda: controller.show_frame("Hill"))
        button5 = tk.Button(self, text="Depth First Search",
                            command=lambda: controller.show_frame("DFS"))
        button6 = tk.Button(self, text="Beam Search",
                            command=lambda: controller.show_frame("Beam"))
        button0 = tk.Button(self, text="Algorithm Analysis",
                            command=lambda: controller.show_frame("Analysis"))
        button5.pack()
        button5.config(relief='solid')
        button2.pack()
        button2.config(relief='solid')
        button3.pack()
        button3.config(relief='solid')
        button4.pack()
        button4.config(relief='solid')
        button6.pack()
        button6.config(relief='solid')
        button1.pack()
        button1.config(relief='solid')
        button0.pack()
        button0.config(relief='solid')


class AStar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Visualization Of A Star Search Algorithm", font=("Helvetica", 10))
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",
                           command=lambda: controller.show_frame("Visualization"))
        button1= tk.Button(self, text="Visualize",
                           command=lambda: vis())
        button1.pack()
        button.pack(side="bottom")



class Dijkstra(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Visualization Of Dijkstra Search Algorithm", font=("Helvetica", 10))
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame("Visualization"))
        button1 = tk.Button(self, text="Visualize",
                            command=lambda: vis1())
        button1.pack()
        button.pack(side="bottom")

class BFS(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Visualization Of Breadth First Search Algorithm", font=("Helvetica", 10))
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame("Visualization"))
        button1 = tk.Button(self, text="Visualize",
                            command=lambda: vis2())
        button1.pack()
        button.pack(side="bottom")

class Hill(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Visualization Of Hill Climbing Search Algorithm", font=("Helvetica", 10))
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame("Visualization"))
        button1 = tk.Button(self, text="Visualize",
                            command=lambda: vis3())
        button1.pack()
        button.pack(side="bottom")

class DFS(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Visualization Of Depth First Search Algorithms", font=("Helvetica", 10))
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame("Visualization"))
        button1 = tk.Button(self, text="Visualize",
                            command=lambda: vis4())
        button1.pack()
        button.pack(side="bottom")


class Beam(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Visualization Of Beam Search Algorithm with Beam width", font=("Helvetica", 10))
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame("Visualization"))
        button1 = tk.Button(self, text="Visualize",
                            command=lambda: vis5())
        button1.pack()
        button.pack(side="bottom")

class Analysis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Algorithm Analysis", font=("Helvetica", 10))
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame("Visualization"))
        button1 = tk.Button(self, text="Visualize Performance Through Graphs",
                            command=lambda: vis7())
        button1.pack()
        button.pack(side="bottom")


if __name__ == "__main__":
    a = Algorithms()
    a.mainloop()
