import matplotlib.pyplot as plt

cells_visited_by_Dijkstra_search = 716
cells_taken_in_path_by_Dijkstra_search = 31
cells_visited_by_Hill_climbing_search = 81
cells_taken_in_path_by_Hill_climbing_search= 41
cells_visited_by_DFS_search = 58
cells_taken_in_path_by_DFS_search = 29
cells_visited_by_A_star_search = 66
cells_taken_in_path_by_A_star_search = 31
cells_taken_in_path_by_Beam_search = 31
cells_visited_by_Beam_search = 81
cells_visited_by_BFS_search= 684
cells_taken_in_path_by_BFS_search = 27

xxx=[cells_taken_in_path_by_A_star_search/cells_visited_by_A_star_search,cells_taken_in_path_by_Dijkstra_search/cells_visited_by_Dijkstra_search ,
  cells_taken_in_path_by_BFS_search/cells_visited_by_BFS_search , cells_taken_in_path_by_Hill_climbing_search/cells_visited_by_Hill_climbing_search,
   cells_taken_in_path_by_DFS_search/cells_visited_by_DFS_search,cells_taken_in_path_by_Beam_search/ cells_visited_by_Beam_search]
x=[1,2,3,4,5,6,7,8]
a=xxx[0]/8
a_star_x = x
a_star_y = []
beam_x= x
beam_y=[]
w=xxx[5]/8
bfs_x= x
bfs_y=[]
g=xxx[2]/8
dfs_x= x
dfs_y=[]
v=xxx[4]/8
hill_x= x
hill_y=[]
o=xxx[3]/8
dij_x= x
dij_y=[]
s=xxx[1]/8
for i in range(1,9):
    a_star_y.append(i*a*2)
    beam_y.append(i*w*2)
    bfs_y.append(i*g*2)
    dfs_y.append(i*v*2)
    hill_y.append(i*o*2)
    dij_y.append(i*s*2)
axis=plt.gca()
axis.set_xlim([0,9])
axis.set_ylim([0,1])
plt.ylabel('Total Cells In Path/Total Cells Visited')
plt.xlabel('Intervals')
plt.plot(a_star_x,a_star_y,color='red')
plt.plot(beam_x,beam_y,color='pink')
plt.plot(bfs_x,bfs_y,color='green')
plt.plot(dfs_x,dfs_y,color='black')
plt.plot(hill_x,hill_y,color='yellow')
plt.plot(dij_x,dij_y,color='purple')
plt.legend(['A Star Search','Beam Search','Breadth First Search','Depth first Search','Hill Climbing Search','Dijkstra Search'], loc='upper left')
plt.show()

