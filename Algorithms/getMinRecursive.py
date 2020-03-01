def find_min(my_list, min = None):
  if len(my_list) == 0:
    return min
  else:
    if min is None or my_list[0] < min:
      min = my_list[0]
  return find_min(my_list[1:], min)