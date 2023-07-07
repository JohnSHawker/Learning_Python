import sys

input_string = str(sys.argv[1])

def is_palindrome(s):
    s = s.lower()
    x = -1
    for letter in s:
        if letter != s[x]:
            return False
        x -= 1
    return True

print(is_palindrome(input_string))