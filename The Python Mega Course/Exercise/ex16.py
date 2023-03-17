"""
Write a program that reads the essay.txt file and returns the number of characters contained in the file.

Add a new member: Solomon Right

Then, the member is added to members.txt. In this case, the text file content would be:

John Smith

Sen Lakmi

Sono Octonot

Solomon Right
"""
new_member = input("Add a new member: ")

file = open(f"../Resources/members.txt", "r")
existing_members = file.readlines()
file.close()

existing_members.append(new_member + "\n")

file = open(f"../Resources/members.txt", "w")
file.writelines(existing_members)
file.close()