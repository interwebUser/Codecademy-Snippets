
def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))


recipe = ["nori", "tuna", "soy sauce", "sushi rice"]
target_ingredient = "avocado"

print(linear_search(recipe, target_ingredient))