def factorial(n): 
  answer = 1
  if n == 0:
    return answer
  while n != 0:
    answer *= n
    n -= 1
  return answer