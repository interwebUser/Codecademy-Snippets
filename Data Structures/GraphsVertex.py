# This program creates a vertex class for use in the Graph Data Structure. 
# This program was written by Khalil Najjar as part of the Codecademy "Career 
# Path: Computer Science" Course, Section 8, Complex Data Structures 


class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

