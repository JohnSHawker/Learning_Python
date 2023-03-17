"""
Create a program that generates multiple text files by iterating over the filenames list.
The text Hello should be written inside each generated text file.

filenames = ["doc.txt", "report.txt", "presentation.txt"]
"""
filenames = ["doc.txt", "report.txt", "presentation.txt"]

for file in filenames:
    document = open(f"../files/{file}", "r")
    existing = document.readlines()
    document.close()

    existing.append("Hello" + "\n")
    
    document = open(f"../files/{file}", "w")
    document.writelines(existing)
    document.close()
