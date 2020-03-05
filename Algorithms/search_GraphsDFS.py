# DFS (Depth-Frist Graph Search Algorithm) is best for long graphs with fewer connections and therefore 
# best at finding if a path exists between two vertices. DFS uses Stack data structure to keep track 
# of the current vertex and vertices that may have unvisited adjacent vertices. 

# BFS (Breadth-First Graph Search Algorithm) is best for densely interconnected graphs and therefore 
# best at finding the shortest path between vertices. BFS uses Queue data structure to keep track of 
# current vertex and vertices that still have neighbors.In BFS graph search a vertex is dequeued 
# when all neighboring vertices have been visited.


def dfs(graph, current_vertex, target_value, visited = None):
  if visited is None:
    visited = []
  visited.append(current_vertex)
  if current_vertex is target_value:
    return visited
  
  for neighbor in graph[current_vertex]:
    if neighbor not in visited:
      path = dfs(graph, neighbor, target_value, visited)
      if path:
        return path
      
def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        if neighbor is target_value:
          return path + [neighbor]
        else:
          bfs_queue.append([neighbor, path + [neighbor]])

some_hazardous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['piranhas', 'bees']),
    'piranhas': set(['bees']),
    'bees': set(['lasers']),
    'lasers': set([])
  }

print(bfs(some_hazardous_graph, 'sharks', 'bees'))
print(dfs(some_hazardous_graph, 'sharks', 'bees'))