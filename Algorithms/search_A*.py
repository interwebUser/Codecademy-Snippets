# The A* (A-star) algorithm is an improvement on Dijkstra's algorithm in that it returns the shortest
# path between a start point and end point, not all paths - through the use of heuristics. This new 
# algorithm is sometimes referred to as a greedy algorithm because it makes a locally optimal choice 
# at every vertex. The heuristic that A* uses makes it an introductory example of artificial intelligence!
# Multiple heuristic types are available for the A* algorithm including Manhattan (x+y) and euclidian 
# (sqrt(x-Distance^2+y-Distance^2)

from math import inf, sqrt
from heapq import heappop, heappush
from search_A_manhattan_graph import manhattan_graph, penn_station, grand_central_station
from search_A_euclidean_graph import euclidean_graph, bengaluru, jaipur

# Manhattan Heuristic:
def heuristic(start, target):
  x_distance = abs(start.position[0] - target.position[0])
  y_distance = abs(start.position[1] - target.position[1])
  return x_distance + y_distance

# Euclidean Heuristic:
#def heuristic(start, target):
#  x_distance = abs(start.position[0] - target.position[0])
#  y_distance = abs(start.position[1] - target.position[1])
#  return sqrt(x_distance**2 + y_distance**2)

def a_star(graph, start, target):
  print("Starting A* algorithm!")
  count = 0
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]
  
  paths_and_distances[start][0] = 0
  vertices_to_explore = [(0, start)]
  while vertices_to_explore and paths_and_distances[target][0] == inf:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight + heuristic(neighbor, target)
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)
        
  print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])
  
  return paths_and_distances[target][1]

