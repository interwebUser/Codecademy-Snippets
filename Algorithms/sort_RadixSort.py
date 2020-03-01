# In our version of least significant digit radix sort, we’re going to utilize
# the string representation of each integer. This, combined with negative 
# indexing, will allow us to count each digit in a number from right-to-left.

# Some other implementations utilize integer division and modular arithmetic 
# to find each digit in a radix sort, but our goal here is to build an 
# intuition for how the sort works.

# The Radix Sort Algorithm does the follow:
# -Takes numbers in an input list.
# -Passes through each digit in those numbers, from least to most significant.
# -Looks at the values of those digits.
# -Buckets the input list according to those digits.
# -Renders the results from that bucketing.
# -Repeats this process until the list is sorted.

def radix_sort(to_be_sorted):
  #determine the size of the largest exponent in our bucket of exponents
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  being_sorted = to_be_sorted[:]

  for exponent in range(max_exponent):
    position = exponent + 1
    index = -position
    
    #create buckets for base-10 exponent
    digits = [[] for i in range(10)]

    for number in being_sorted:
      number_as_a_string = str(number)
      try:
        digit = number_as_a_string[index]
      except IndexError:
        digit = 0
      digit = int(digit)

      digits[digit].append(number)

    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  return being_sorted

unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]

print(radix_sort(unsorted_list))