def multiplication(num_1, num_2):
  if num_1 == 0 or num_2 == 0:
    return 0
  return (num_1 + multiplication(num_1, num_2 - 1))