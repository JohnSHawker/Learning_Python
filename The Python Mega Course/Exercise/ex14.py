"""
Please download the essay.txt file from the resources of this article. Then, create a program that reads that file and
prints out its text. The first letter of each word in the output should be uppercase.
"""
file = open(f"../Resources/essay.txt", "r")
text = file.read()
print(text.title())
file.close()

