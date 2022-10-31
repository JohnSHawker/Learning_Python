# import re

# my_string = "A quick brown fox jumped over the lazy dog."

# def remove_vowels(my_string):
#     my_string = re.sub("[a,e,i,o,u,A,E,I,O,U]", "*", my_string)
#     print(my_string)

# remove_vowels(my_string)

my_string = "Calvin and Hobbes"
vowels = "aeiouAEIOU"

for vowel in vowels:
    my_string = my_string.replace(vowel, "*")

print(my_string)