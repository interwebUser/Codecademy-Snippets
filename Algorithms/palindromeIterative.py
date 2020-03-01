# Quadratic Runtime - O(N^2)
#
# def is_palindrome(my_string):
#   while len(my_string) > 1:
#     if my_string[0] != my_string[-1]:
#       return False
#     my_string = my_string[1:-1]
#   return True 

# Linear Runtime - O(N)
def is_palindrome(my_string):
  string_length = len(my_string)
  middle_index = string_length // 2
  for index in range(0, middle_index):
    opposite_character_index = string_length - index - 1
    if my_string[index] != my_string[opposite_character_index]:
      return False  
  return True