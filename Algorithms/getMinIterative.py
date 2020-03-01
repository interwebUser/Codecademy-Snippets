def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min