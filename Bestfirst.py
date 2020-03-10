import time
import Board5 as Board
import math

Board.window.title("Beam Search")

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
        return list(results)

rows = Board.rows
cols = Board.cols
Width = Board.Width
start = Board.player
goal = Board.end


diagram1 = SquareGrid(cols,rows)
diagram1.walls = Board.Walls

import threading

beamwidth=1

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def getheuristic(lst,n2):
    t=[]
    r=[]
    for i in lst:
        t.append((heuristic(n2,i),i))
    g=0
    for i in range(len(t)):
        mini=t[i][0]
        g=i
        for j in range(i+1,len(t)):
            if mini>t[j][0]:
                mini=t[j][0]
                g=j
        t[i],t[g]=t[g],t[i]
    for i in t:
        r.append(i[1])
    return r

def beam(graph,start,end):
   global beamwidth
   visited=[start]
   q=[start]
   level={}
   level[start]=0
   parent={}
   parent[start]=None
   level_of_neighbors=0
   a=1
   while len(q)!=0:
       t=[]
       for i in q:
           if level[i]==level_of_neighbors:
               t.append((i))
       s=getheuristic(t,end)
       s=s[math.ceil(beamwidth/a):]
       if s!=[]:
           for i in s:
               q.remove(i)
       current = q.pop(0)
       if current == end:
           print("Goal Reached using Beam Search")
           break
#       if current!=end:
#           print(beamwidth)
#           beamwidth+=1

       z=sorted(graph.neighbors(current))
       x=(getheuristic(z,end))
       for i in x:
            if i not in visited:
               q.append(i)
               visited.append(i)
               level[i]=level[current]+1
               level_of_neighbors=level[current]+1
               a=len(graph.neighbors(i))
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


came_from = beam(diagram1, start, goal)
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