name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.lower())
print(name.upper())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

#.title(), .upper(), and .lower() are methods
#.title() will cappitalize the first letter in the string
#.upper() will capitalize the entire string
#.lower() will lowercase the entire string, this is usefull for storing user input information.


# using an octothorpe at the beginning of your line will turn it into a comment.

print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# adding \t to your text will put a tab space infront of the text
# adding \n to your text will move the following text to a new line
# using the rstrip() method will remvoe white space on the right side of a string
# using the lstrip() method will remove white space on the left side of a string
# using the strip() method will remove white space from the left and right side of a string

favorite_language = ' Python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
