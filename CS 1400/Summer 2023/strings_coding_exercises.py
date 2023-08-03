# -----------------------------------------------------------------------------
# problem 1
# -----------------------------------------------------------------------------

user_input = input()
first = user_input[0]
last = user_input[-1]
print(f"{first} is the first character and {last} is the last character")

# -----------------------------------------------------------------------------
# problem 2
# -----------------------------------------------------------------------------

user_input = input()
length = len(user_input)
i = 0
while i != length:
    print(user_input * length)
    i += 1

# -----------------------------------------------------------------------------
# problem 3
# -----------------------------------------------------------------------------

user_input = input()
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
new_string = ""
for char in user_input:
    if char in upper:
        new_string += "u"
    elif char in lower:
        new_string += "l"
    else:
        new_string += "-"
print(new_string)

# -----------------------------------------------------------------------------
# problem 4
# -----------------------------------------------------------------------------

user_input = input()

length = len(user_input)
midpoint = length // 2

first_half = user_input[:midpoint]
second_half = user_input[midpoint:]

print(first_half)
print(second_half)

# -----------------------------------------------------------------------------
# problem 5
# -----------------------------------------------------------------------------

txt = input()
length = len(txt)
swapped_string = ""

for i in range(0, length - 1, 2):
    swapped_string += txt[i + 1]
    swapped_string += txt[i]

print(swapped_string)
