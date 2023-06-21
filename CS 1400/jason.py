"""
This is the answer to problem 1
"""

new_list = []

for number in numbers:
  if number > 10:
    new_list.append('*')
  else:
    new_list.append(number)

print(new_list)

# numbers = [1, 2, 23, 42]
# print([x if x < 10 else "*" for x in numbers])

"""
This is the answer to problem 2
"""

# if len(my_list) < 5:
#   print(my_list * 3)
# else:
#   print(my_list)


if len(my_list) < 5:
    print(my_list + my_list + my_list)
else:
    print(my_list)

"""
This is the answer to problem 3
"""

strings.sort()
print(strings[0])

"""
This is the answer to problem 4
"""
# numbers = [1, 3, 5, 7]

diff = numbers[1] - numbers[0]
max_num = max(numbers)
numbers.append(max_num + diff)
numbers.append(max_num + diff + diff)
  
print(numbers)

"""
This is the answer to problem 5
"""

# import sys

# number = int(sys.argv[1])
# data = [[0 for i in range(number)] for j in range(number)]

for i in range(number):
  data[i][i] = 1

for sublist in data:
  for element in sublist:
    print(element, end = ' ')
  print('')
