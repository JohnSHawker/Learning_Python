"""
Write a program that reads the essay.txt file and returns the number of characters contained in the file.
"""
file = open(f"../Resources/essay.txt", "r")
content = file.read()
print(len(content))
file.close()