# How Dijkstra's Algorithm works in Python:
# 1. Instantiate a dictionary that will eventually map vertices to their distance from their start vertex
# 2. Assign the start vertex a distance of 0 in a min heap
# 3. Assign every other vertex a distance of infinity in a min heap
# 4. Remove the vertex with the smallest distance from the min heap and set that to the current vertex
# 5. For the current vertex, consider all of it’s adjacent vertices and calculate the distance to them by (distance to the current vertex) + (edge weight of current vertex to adjacent vertex). If this new distance is less than its current distance, replace the distance.
# 6. Repeat 4 and 5 until the heap is empty
# 7. After the heap is empty, return the distances
# This algorithm has a runtime of O((V+E)logV) where V = # of vertices and E = # of edges

from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }


def dijkstras(graph, start):
    # create dictionary to map vertices to their distance from start vertex
  distances = {}
  
  for vertex in graph:
    # assign every other vertex a distance of infinity in min heap
    distances[vertex] = inf

  # assign start vertex a distance of 0 in min heap  
  distances[start] = 0
  # instantiate a tuple to keep track of vertices to explore and their weights back to the starting vertex
  vertices_to_explore = [(0, start)]
  
  # while the min heap is not empty
  while vertices_to_explore:
    # remove the vertex with the minimum distance from the min heap and set it to the current vertex
    current_distance, current_vertex = heappop(vertices_to_explore)
    
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      
      # if new distance is less than its current distance set the new current distance of the neighbor to 
      # the new distance
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
        
  return distances
        
distances_from_d = dijkstras(graph, 'D')
print("\n\nShortest Distances: {0}".format(distances_from_d))

