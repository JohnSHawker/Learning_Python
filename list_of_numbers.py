# from cgitb import small


# my_list = [14, 56, 71, 29, 40, 11]
# total = sum(my_list)
# largest = max(my_list)
# smallest = min(my_list)
# print(total)
# print(largest)
# print(smallest)

# my_list = [11, 71, 65, 42, 3]
# print(3 in my_list)

import sys

numbers = sys.argv[1:]
for i in range(len(numbers)):
  numbers[i] = int(numbers[i])

print(numbers)