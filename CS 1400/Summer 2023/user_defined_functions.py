# Problem 1

"""
Problem
Write a function called avg that takes two parameters.
Return the average of these two parameters. If the parameters are not numbers, return the string, Please use two numbers as parameters.

Expected Output
If the function call is avg(10,25), then the function would return 17.5
If the function call is avg(10, "cat"), then the function would return Please use two numbers as parameters
"""

# def avg(par1, par2):
#     try:
#         return(par1 + par2) / 2
#     except TypeError:
#         return("Please use two numbers as parameters")

# Their answer:

# def avg(n1, n2):
#     """Return average of two numbers
#     Return a message is a non-number is passed"""
#     try:
#       return(n1 + n2) / 2
#     except TypeError:
#       return("Please use two numbers as parameters")

#------------------------------------------------------------------------------------------
# Problem 2

"""
Problem
Write a function called odds_or_evens that takes a boolean and a list of integers as parameters.
If the boolean parameter is True, return a list of only even numbers. If the boolean parameter isFalse, return a list of only odd numbers.

Expected Output
If the function call is odds_or_evens(True, [13, 22, 8, 31]), the the function would return [22, 8]
If the function call is odds_or_evens(False, [13, 22, 8, 31]), the the function would return [13, 31]
"""

# def odds_or_evens(t_or_f, list):
#     if t_or_f == True:
#         even_list = []
#         for number in list:
#             if number % 2 == 0:
#                 even_list.append(number)
#         print(even_list)
#         return even_list
#     else:
#         odd_list = []
#         for number in list:
#             if number % 2 != 0:
#                 odd_list.append(number)
#         print(odd_list)
#         return odd_list

# odds_or_evens(True, [13, 22, 8, 31])
# odds_or_evens(False, [13, 22, 8, 31])

# Their answer:

# def odds_or_evens(my_bool, nums):
#     """Returns all of the odd or
#     even numbers from a list"""
#     return_list = []
#     for num in nums:
#       if my_bool:
#           if num % 2 == 0:
#               return_list.append(num)
#       else:
#           if num % 2 != 0:
#               return_list.append(num)

#     return return_list

#------------------------------------------------------------------------------------------
# Problem 3

"""
Problem
Write a function called search_list that takes a list and a search term as parameters.
If the search term is located in the list, return the index of the matching element.
The function should work even if there is a difference in capitalization.
If the search term is not in the list, return -1.

Expected Output
If the function call is search_list(["dog", "fish", "cat"], "Cat"), the the function would return 2
If the function call is search_list(["water", "Toy", "house"], "toy"), then the function would return 1
If the function call is search_list(["box", "car", "hat"], "mouse"), the the function would return -1
"""


# def search_list(list, search_term):
#     search_term = search_term.lower()
#     index = 0
#     length_of_list = len(list) - 1
#     for word in list:
#         word = word.lower()
#         if word == search_term:
#             print(index)
#             return index
#         index += 1
#         if index > length_of_list:
#             print(-1)
#             return -1

# search_list(["dog", "fish", "cat"], "Cat")
# search_list(["water", "Toy", "house"], "toy")
# search_list(["box", "car", "hat"], "mouse")

# Their answer:

# def search_list(lst, term):
#     """Search for item in a list
#     Return the index if found
#     Return -1 if not found"""
#     for item in lst:
#         if item.lower() == term.lower():
#             return lst.index(item)
#     return -1

#------------------------------------------------------------------------------------------
# Problem 4

"""
Problem
Write a function called best_team that takes a csv file as a parameter. Read the comma-delimited CSV file specified by the variable mlb_data.
The CSV file has a list of all of the MLB teams and their performance from the 2019 season.
The function should return the team name for the team with the most wins.
Important, the CSV file has a header of Tm,Lg,G,W,L, which stands for team name, league, games played, wins, and losses.
Below are the file name and file path variables you will need for this exercise.

mlb_data = "student_folder/.exercises/mlb_data.csv"

Expected Output
The function call should look like this, best_team(file), and the function should return HOU.
However, your function will be tested with other CSV files in which different teams will have the highest win total.
"""

import sys
import os
import csv

def best_team(file):
    mlb_data = "student_folder/.exercises/mlb_data.csv"
    with open(mlb_data, "r") as input_file:


# Their answer:

import csv

mlb_data = "student_folder/.exercises/mlb_data.csv"

def best_team(file):
    ""Read a CSV of baseball data.
    Return the team name with the most wins""
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        most_wins = 0
        best_team = ""
        for row in reader:
            if int(row[3]) > most_wins:
                most_wins = int(row[3])
                best_team = row[0]
        return best_team


#------------------------------------------------------------------------------------------
# Problem 5
"""
Problem
Write a function called is_palindrome that takes a string as a parameter.
The function will return True if the string is a palindrome (is the same forward and backward).
The function will return False if the string is not a palindrome.

Expected Output
If the function call is is_palindrome("level"), the the function would return True
If the function call is is_palindrome("house"), the the function would return False

Important
Do not use a helper function for this problem. Though this is good situation in which to use one,
the auto-grader only works if all of the coding is done inside the is_palindrome function.
"""

# Their answer:

def is_palindrome(string):
    reversed_string= ""
    position = len(string) - 1
    while position >= 0:
        reversed_string += string[position]
        position -= 1
    if string == reversed_string:
        return True
    else:
        return False