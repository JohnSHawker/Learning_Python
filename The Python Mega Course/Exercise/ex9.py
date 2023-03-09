"""
Coding Exercise 1
Create a program that:

1. Prompts the user to input a (dollar) amount.

2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.

3. Prints out the amount in euros, as shown in the screenshot below.

How many dollars have you got? 100
The amount in euros is:
95.0
"""
user_usd = int(input("How many dollars have you got? "))
user_euro = user_usd * 0.95
print(f"The amount in euros is:\n",user_euro)
