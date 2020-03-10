import time
import Board
import random

Board.window.title("A Star Search")


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def cost(self,from_node, to_node):
        return random.randint(0,Board.rows)


rows = Board.rows
cols = Board.cols
Width = Board.Width
start = Board.player
goal = Board.end


diagram1 = SquareGrid(cols,rows)
diagram1.walls = Board.Walls

import heapq
import threading

class PriorityQueue:
    def __init__(self):
        self.elements = []
    def empty(self):
        return len(self.elements) == 0
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    def get(self):
        return heapq.heappop(self.elements)[1]

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(graph, start, goal):
    Q = PriorityQueue()
    Q.put(start,0)
    parent = {}
    dist = {}
    dist[start] = 0
    parent[start] = None
    while not Q.empty():
        currentcell = Q.get()

        if currentcell == goal:
            print ("Goal Reached using A Star Search")
            break
        for next in graph.neighbors(currentcell):
            approx_cost = dist[currentcell] + graph.cost(currentcell,next)
            if next not in dist or approx_cost < dist[next]:
                dist[next] = approx_cost
                priority = heuristic(goal, next)
                Q.put(next, priority)
                parent[next] = currentcell

    return parent, dist

def trivialpath(came_from,cost_so_far,start,goal):
    path=[]
    q=len(cost_so_far)
    while (q)!=0:
        for i in cost_so_far:
            a=reconstruct_path(came_from, start, i)
            path.append(a)
            q-=1
    return path

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

parent, dist = a_star(diagram1, start, goal)
total_path = reconstruct_path(parent, start, goal)
trivial_path = trivialpath(parent,dist,start,goal)

m,n=len(parent),len(total_path)
print('Total Cells Visited: ',m)
print('Total Cells Taken In Path: ',n)
print('Total Walls In The Board: ',len(Board.Walls))

def run():
    global total_path
    global trivial_path
    Board.render_trivial_path(trivial_path)
    Board.render_path(total_path)
    time.sleep(10)
    Board.window.destroy()

t = threading.Thread(target=run)
t.daemon = True
t.start()
Board.start_game()