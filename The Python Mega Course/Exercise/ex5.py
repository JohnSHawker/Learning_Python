"""
Coding Exercise 2
Create a program that prompts the user to input their name once. Then, the program repeatedly prints out the name with
the first letter capitalized.
"""
userinput = input("What is your name? ")
number = 0

while number <= 3:
    print(userinput.capitalize())
    number = number + 1