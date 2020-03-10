import time
import random
import Board1 as Board

Board.window.title("Dijkstra Search")

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

import threading

def dijkstra(G,n1,n2):
    shortestdistance={}
    predecessors={}
    seenNodes=[n1]
    predecessors[n1]=None
    infinity=float('inf')
    t=[n1]
    while len(t)!=0:
        a=t.pop()
        shortestdistance[a]=infinity
        for i in G.neighbors(a):
            if i not in shortestdistance:
                t.append(i)
    shortestdistance[n1] = 0
    while len(seenNodes)!=0:
        minNode=None
        for node in seenNodes:
            if minNode is None:
                minNode=node
            elif shortestdistance[node]<shortestdistance[minNode]:
                minNode=node
        current = seenNodes.pop(seenNodes.index(minNode))
        for childNode in G.neighbors(current):
            if childNode not in seenNodes:
                weight=G.cost(current,childNode)
                if weight + shortestdistance[current]<shortestdistance[childNode]:
                   shortestdistance[childNode]=weight+shortestdistance[current]
                   predecessors[childNode]=current
                   seenNodes.append(childNode)
    return predecessors,shortestdistance

def trivialpath(came_from,start):
    path=[]
    q=len(came_from)
    while (q)!=0:
        for i in came_from:
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

came_from, cost_so_far = dijkstra(diagram1, start, goal)
total_path = reconstruct_path(came_from, start, goal)
trivial_path = trivialpath(came_from,start)

n=len(came_from)
m=len(total_path)

print('Goal Reached using Dijsktra Search')
print('Total Cells Visited: ',n)
print('Total Cells Taken In Path: ',m)
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