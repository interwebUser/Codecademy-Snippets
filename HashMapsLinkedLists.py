# This program creates a hash map with the ability to write and read key:value pairs
# to an array of size specified by the user. It also uses an Linked Lists technique
# for handling collisions. Note that the Linked Lists are imported from another file
# to save real estate in this file. This program was written by Khalil Najjar as part
# of the Codecademy "Career Path: Computer Science" Course, Section 8, Complex Data Structures 


#Importing LinkedList functionality
from linked_list import Node, LinkedList

class HashMap:
  def __init__(self, size):
    self.array_size = size
    # modify code to work with linked list instead.
    # self.array = [None for i in range(self.array_size)]
    self.array = [
      LinkedList() for i in range(size)
    ]
    
  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code
  
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    hash_code = hash(key)
    array_index = self.compress(hash_code)
    #Hash Assignment Logic to be replaced:
    #self.array[array_index] = [key, value]
    
    #Node Assignment Logic:
    payload = Node([key,value])
    list_at_array = self.array[array_index]
    for i in list_at_array:
      if i[0] == key:
        i[1] = value
      return
    list_at_array.insert(payload)
  
  def retrieve(self, key):
    hash_code = hash(key)
    array_index = self.compress(hash_code)
    # retrieval logic replaced with Separate Chaining
    # payload = self.array[array_index]
    # if payload[0] == key:
    #   return payload[1]
    # if payload is None or payload[0] != key:
    #   return None
    list_at_index = self.array[array_index]
    for i in list_at_index:
      if i[0] == key:
        return i[1]
      else:
        return None
    return
  
hair = [
  ["khalil", "brown"],
  ["islam", "black"],
  ["haneen", "brown"],
	["alina", "blond"]
]

beauty = HashMap(len(hair))
for person in hair:
  beauty.assign(person[0], person[1])

print(beauty.retrieve("khalil"))
print(beauty.retrieve("haneen"))
print(beauty.retrieve("islam"))
print(beauty.retrieve("alina"))