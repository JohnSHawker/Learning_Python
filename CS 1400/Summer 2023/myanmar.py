"""
Write a program that reads the text file student_folder/.labs/myanmar.txt.
The file contains several instances of the word Burma. Replace each instance of Burma with Myanmar,
and print the results of this transformation. The final output of your program should be:
Myanmar is a country in Southeast Asia.
The capital of Myanmar is Naypyidaw.
Its population is about 54 million people.
Myanmar is a former British colony.
"""
# Their answer:
with open("student_folder/.labs/myanmar.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        if "Burma" in line:
            print(line.replace("Burma", "Myanmar"), end="")
        else:
            print(line, end="")

# My answer (not working):
# new_list = []
# with open("student_folder/.labs/myanmar.txt", "r") as source:
#     new_list = source.readlines()

# output = []
# with open("student_folder/.labs/myanmar2.txt", "w") as dest:
#     for i in new_list:
#         i = i.split(" ")
#         for j in range(len(i)):
#             if i[j] == "Burma":
#                 i[j] = "Myanmar"
#         output.append(i)
#     print(output)
#     for i in output:
#         for j in i:
#             if len(j) > 2:
#                 if j[-2] == '\\' and j[-1] == "n":
#                     dest.write(j)
#                 else:
#                     dest.write(j + " ")
#             else:
#                 dest.write(j + " ")

"""
Problem 1
"""

import sys

test_file = sys.argv[1]
lin = 0
characters = 0
with open(test_file, "r") as input_file:
  lines = input_file.readlines()
  lin = len(lines)
  for line in lines:
    for char in line:
      characters = len(char) + characters
  print(f"{lin} lines")
  print(f"{characters} characters")


"""
Problem 2
"""

import sys
import csv

test_file = sys.argv[1]

total1 = 0
total2 = 0
total3 = 0
total4 = 0
row_count = 0

with open(test_file, "r") as input_file:
  reader = csv.reader(input_file)
  for num1, num2, num3, num4 in reader:
    row_count += 1
    total1 += int(num1)
    total2 += int(num2)
    total3 += int(num3)
    total4 += int(num4)

print(f"{total1 / row_count} {total2 / row_count} {total3 / row_count} {total4 / row_count}")

"""
Problem 3
"""

import sys

test_file = sys.argv[1]

with open(test_file, "r") as input_file:
  lines = input_file.readlines()
  lines.reverse()
  for line in lines:
    print(f"{line}\n")

"""
Problem 4
"""

import sys
import csv

test_file = sys.argv[1]

oldest_age = 0
oldest_name = ""

with open(test_file, "r") as input_file:
  lists = csv.reader(input_file, delimiter='\t')
  next(lists)
  for name, age, career, in lists:
    if int(age) > oldest_age:
      oldest_age = int(age)
      oldest_name = name


  print(f"The oldest person is {name}.")

"""
Problem 5
"""

import sys
import csv

test_file = sys.argv[1]
city_names = []
new_list = []

with open(test_file, "r") as input_file:
  lists = csv.reader(input_file)
  next(lists)
  for city, country, latitude, longitude in lists:
    if int(latitude) < 0:
      city_names.append(city)

  print(f"The following cities are in the Southern Hemisphere:", end = " ")
  for cities in city_names:
    if cities == city_names[-1]:
      print(cities, end = ".")
    else:
      print(cities, end = ", ")