"""Exercise 1"""
word = input()
first_char = word[:1]
last_char = word[-1:]
print(f"{first_char} is the first character and {last_char} is the last character")

"""Exercise 2"""
word = input()
i = 0
for i in range(len(word)):
    print(word * len(word))

"""Exercise 3"""
string1 = input()
string2 = ""
for letter in string1:
    if letter.isupper():
        string2 += "u"
    elif letter.islower():
        string2 += "l"
    else:
        string2 += "-"

print(string2)

"""Exercise 4"""
string1 = input()
middle = len(string1) // 2
string2 = string1[:middle]
string3 = string1[middle:]
print(string2)
print(string3)

"""Exercise 5"""
txt = input()
length = len(txt)
swapped_string = ""

for i in range(0, length - 1, 2):
    swapped_string += txt[i + 1]
    swapped_string += txt[i]

print(swapped_string)