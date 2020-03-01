def sum_digits(n):
  if n <= 9:
    return n
  new_n = n % 10
  return new_n + sum_digits(n // 10)