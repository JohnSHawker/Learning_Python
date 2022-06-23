# search_text = "Burma"
# replace_text = "Myanmar"

# with open("student_folder/.labs/myanmar.txt", "r") as file:
#     data = file.read()
#     data = data.replace(search_text, replace_text)

# with open("student_folder/.labs/myanmar.txt", "w") as file:
#     file.write(data)

# with open("student_folder/.labs/myanmar.txt", "r") as input_file:
#     lines = input_file.readlines()
#     for line in lines:
#         if "Burma" in line:
#             print(line.replace("Burma", "Myanmar"), end="")
#         else:
#             print(line, end="")

import sys

test_file = sys.argv[1]

line_count = 0
char_count = 0

with open(test_file, "r") as input_file:
    line = input_file.readline()
    while line != "":
        line_count += 1
        char_count += len(line)
        line = input_file.readline()

print("{} lines".format(line_count))
print("{} characters".format(char_count))