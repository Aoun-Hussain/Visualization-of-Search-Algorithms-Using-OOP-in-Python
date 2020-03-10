import time
import Board2 as Board

Board.window.title("Breadth First Search")

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

rows = Board.rows
cols = Board.cols
Width = Board.Width
start = Board.player
goal = Board.end


diagram1 = SquareGrid(cols,rows)
diagram1.walls = Board.Walls

import threading

def bfs(graph,start,end):
   visited=[start]
   q=[start]
   level={}
   level[start]=0
   parent={}
   parent[start]=None
   while len(q)!=0:
       current = q.pop(0)
       if current == end:
           print("Goal Reached using BFS Search")
           break
       for i in sorted(graph.neighbors(current)):
           if i not in visited:
               q.append(i)
               visited.append(i)
               level[i]=level[current]+1
               parent[i]=current
#   print ('Level of Nodes: ',level)
#   print ("Parent of Each Node: " ,parent)
#   print ("Breadth First Traversal: ",v)
   return parent

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


came_from = bfs(diagram1, start, goal)
total_path = reconstruct_path(came_from, start,goal)
trivial_path = trivialpath(came_from,start)

n=len(came_from)
m=len(total_path)
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