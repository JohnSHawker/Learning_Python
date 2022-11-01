# def rotate_word(strings, integers):
#     result = ""
#     for i in range(len(strings)):
#         char = strings[i]
#         if (char.isupper()):
#             result += chr((ord(char) + integers-65) % 26 + 65)
#         else:
#             result += chr((ord(char) + integers - 97) % 26 + 97)
#         return result
# print( rotate_word( input(), int(input())))

"""A python program to illustrate Caesar Cipher Technique"""
def encrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result

print( encrypt( input(), int(input()) ) )
# #check the above function
# text = "ATTACKATONCE"
# s = 4
# print ("Text : " + text)
# print ("Shift : " + str(s))
# print ("Cipher: " + encrypt(text,s))


def rotate_word(text,shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
        return result
print( rotate_word( input(), int(input())))