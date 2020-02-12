# This program creates a Tree data structure with the ability to add and remove nodes
# and traverse the tree.
# This program was written by Khalil Najjar as part of Codecademy's "Career Path: 
# Computer Science" Course, Section 8, Complex Data Structures 

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)
    
  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children
    

root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")
third_child = TreeNode("Marketing Assistant")
fourth_child = TreeNode("Head of Finance")

root.add_child(first_child)
root.add_child(second_child)
second_child.add_child(third_child)
root.add_child(fourth_child)
root.traverse()