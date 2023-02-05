"""
Coding Exercise 3
Create a program that prompts the user to input their name repeatedly. Then, the program repeatedly prints out the name
with the first letter capitalized.

In other words, the program should behave as in the screenshot below:

What is your name? ardit
Ardit
What is your name? ben
Ben
What is your name? john
John
What is your name?
"""
while True:
    userinput = input("What is your name? ")
    print(userinput.capitalize())