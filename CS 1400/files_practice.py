"""
Exercise 1

Problem:
Write a program that reads a text file and returns the number of lines as well as the total number of characters in the file.

Hint:
to open the file use with open(test_file, "r".... The TRY IT button below will send a test file to your program. 
You should see the following output:
    4 lines
    231 characters

The first two lines of your code must look like this:
    import sys

    test_file = sys.argv[1]
"""
#Exercise 1
import sys
# import sys allows the program to use system inputs
test_file = sys.argv[1]
# sys.argv[1] is referencing the index in the list from sys when the program opens
line_count = 0
char_count = 0
# we want to find these interger values so we set the starting int to 0
with open(test_file, "r") as test:
    for line in test:
        line_count += 1
        char_count += len(line)
# open test_file as a readable file we called it test
# for line in test will iterate through each line in the varable called test
# upon each iteration the line_count will increase in value by 1
# upon each iteration the char_count will increase by the length of the string in that line
# now test will close automatically since we used the with open() function
print(f"{line_count} lines")
print(f"{char_count} characters")

"""
Exercise 2

Problem:
Write a program that reads a comma delimited CSV file with four columns and returns the average of each column in the file.

Hint:
to open the file use with open(test_file, "r".... The TRY IT button below will send a test file to your program.
You should see the following output:
    10.0 8.0 6.0 20.0

The first two lines of your code must look like this:
    import sys

    test_file = sys.argv[1]
"""
#Exercise 2
import sys
import csv
# needed to use the csv module to read the file correctly
test_file = sys.argv[1]

col1 = 0
col2 = 0
col3 = 0
col4 = 0
row_count = 0
# need each column assigned its own variable and will divide the sum of each
# column by the number of rows to get the average value of each column
with open(test_file, "r") as test:
  reader = csv.reader(test)
  for number1, number2, number3, number4 in reader:
    # The number1 - number4 will assign to values in the csv file on each row
    # for each iteration
    col1 += int(number1)
    col2 += int(number2)
    col3 += int(number3)
    col4 += int(number4)
    row_count += 1

print(f"{col1/row_count} {col2/row_count} {col3/row_count} {col4/row_count}")

"""
Exercise 3

Problem:
Write a program that reads a text file and prints the contents in reverse order.

Hint:
to open the file use with open(test_file, "r".... The TRY IT button below will send a test file to your program.
You should see the following output:
    The child still struggled and loaded me with epithets which carried despair to my heart; I grasped his throat to 
    silence him, and in a moment he lay dead at my feet.
    ‘Frankenstein! you belong then to my enemy—to him towards whom I have sworn eternal revenge; you shall be my first
    victim.’
    ‘Hideous monster! Let me go. My papa is a syndic—he is M. Frankenstein—he will punish you. You dare not keep me.’
    ‘Boy, you will never see your father again; you must come with me.’
    He struggled violently. ‘Let me go,’ he cried; ‘monster! Ugly wretch! You wish to eat me and tear me to pieces. 
    You are an ogre. Let me go, or I will tell my papa.’

The first two lines of your code must look like this:
    import sys

    test_file = sys.argv[1]
"""
#Exercise 3
import sys

test_file = sys.argv[1]

with open(test_file, "r") as input_file:
    lines = input_file.readlines()
    lines.reverse()
    for line in lines:
        print(line)

"""
Exercise 4

Problem:
Write a program that reads a tab delimited CSV file and prints the name of the oldest person in the file.

Hint:
there will be a row with header titles.

The first two lines of your code must look like this:
    import sys, csv

    test_file = sys.argv[1]
"""
#Exercise 4
import sys
import csv

test_file = sys.argv[1]

oldest_age = 0
oldest_name = ""

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file, delimiter="\t")
    next(reader)
    for name, age, career in reader:
        if int(age) > oldest_age:
            oldest_age = int(age)
            oldest_name = name

print(f"The oldest person is {oldest_name}.")

"""
Exercise 5

Problem:
Write a program that reads a comma delimited CSV file and prints all of the cities which reside in the Southern Hemisphere.

Hint:
any latitude with a negative value is south of the equator. there will be a row with header titles.

The first two lines of your code must look like this:
    import sys, csv

    test_file = sys.argv[1]
"""
#Exercise 5
import sys
import csv

test_file = sys.argv[1]

southern_cities = ""

with open(test_file, "r") as input_file:
  reader = csv.reader(input_file)
  next(reader)
  for city, country, latitude, longitude in reader:
    if int(latitude) < 0:
      southern_cities += city + ", "

southern_cities = southern_cities[:-2]
print(f"The following cities are in the Southern Hemisphere: {southern_cities}.")