'''
Project Name: Rabbits, Rabbits, Rabbits
Author: John Hawker
Due Date: 2022-06-18
Course: CS1400-X01

This program will take the input parameters from run_rabbits.py and feed them into my do_research function.
The function will output data into the file rabbits.csv
'''
import os
import csv

def do_research(cages, adults, babies):
    
    months = 1
    total = adults + babies
    with open("rabbits.csv", "w") as output_file:
        output_file.writelines("# Table of rabbit pairs\n")
        output_file.writelines("Month, Adults, Babies, Total\n")
        
    while total < cages:
        total = adults + babies
        with open("rabbits.csv", "a") as output_file:
            output_file.writelines(f"{months}, {adults}, {babies}, {total}\n")
        babies = adults
        adults = total
        months += 1
    
    with open("rabbits.csv", "a") as output_file:
        output_file.writelines(f"# Cages will run out in month {months - 1}")

do_research(500, 1, 0)