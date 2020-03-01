def fibonacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  fib_list = [0, 1]
  if n <= len(fib_list):
    return fib_list[n]
  else:
    while n > (len(fib_list) - 1):
      next_fib = fib_list[-1] + fib_list [-2]
      fib_list.append(next_fib)
  return fib_list[n]