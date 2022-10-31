"""Exercise 1"""
def avg(n1, n2):
    try:
      return(n1 + n2) / 2
    except TypeError:
      return("Please use two numbers as parameters")

"""Exercise 2"""
def odds_or_evens(my_bool, nums):
  return_list = []
  for num in nums:
    if my_bool:
      if num % 2 == 0:
        return_list.append(num)
    else:
      if num % 2 != 0:
        return_list.append(num)
  return return_list

"""Exercise 3"""
def search_list(my_list, keyword):
    for item in my_list:
      if item.lower() == keyword.lower():
        return my_list.index(item)
    return -1
    
"""Exercise 4"""
import csv

mlb_data = "student_folder/.exercises/mlb_data.csv"

def best_team(file):
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

"""Exercise 5"""
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False