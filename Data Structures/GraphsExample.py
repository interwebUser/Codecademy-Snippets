# The Graph data structure implemented here is deisnged with the following in mind:

# Vertex:
# Uses a dictionary as an adjacency list to store connected vertices.
# Connected vertex names are keys and the edge weights are values.
# Has methods to add edges and return a list of connected vertices.

# Graph:
# Can be initialized as a directed graph, where edges are set in one direction.
# Stores every vertex inside a dictionary
#   Vertex data is the key and the vertex instance is the value.
# Has methods to add vertices, edges between vertices, and determine if a path 
# exists between two vertices.from random import randrange

from GraphsGraph import Graph
from GraphsVertex import Vertex
from random import randrange

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)


def build_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  for v in range(len(vertices)):
    v_idx = randrange(0, len(vertices) - 1)
    v1 = vertices[v_idx]
    v_idx = randrange(0, len(vertices) - 1)
    v2 = vertices[v_idx]
    g.add_edge(v1, v2, randrange(1, 10))

  print_graph(g)

build_graph(False)

