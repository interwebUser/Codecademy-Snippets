def is_palindrome(my_string):
  if len(my_string) < 2:
    return True
  if my_string[0] != my_string[-1]:
    return False
  return is_palindrome(my_string[1:-1])