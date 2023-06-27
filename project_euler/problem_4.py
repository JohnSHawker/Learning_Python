"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is: 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
numbers = []
for i in range(1000):
    for j in range(1000):
        numbers.append(i * j)
print(len(numbers))
# print(numbers)