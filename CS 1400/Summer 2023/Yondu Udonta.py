'''
Project Name: Yondu Udonta
Author: John Hawker
Due Date: 05/26/2023
Course: CS1400-X02

This program takes a user input for the number of Reavers and a user input for the number of units.
The program then calculates the number of units Yondu receives, Peter receives, each crew member receives,
and how many units go to the RBF
'''

def main():
    '''
    Program starts here.
    '''
    try:
        # (1) replace pass with your code
        reavers = int(input("How many Reavers: "))
        units = int(input("How many units: "))

    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    # (2) replace pass with your code
    number_of_reavers = reavers
    number_of_units = units
    crew_leave_cost = (number_of_reavers - 2) * 3
    number_of_units = number_of_units - crew_leave_cost
    yondu_13_percent = number_of_units // (1 / 0.13)
    number_of_units = number_of_units - yondu_13_percent
    peter_11_percent = number_of_units // (1 / 0.11)
    number_of_units = number_of_units - peter_11_percent
    crew_pay = number_of_units // number_of_reavers
    rbf = number_of_units - (number_of_reavers * crew_pay)
    yondu_total = yondu_13_percent + crew_pay
    peter_total = peter_11_percent + crew_pay
    print("Yondu's share:", int(yondu_total))
    print("Peter's share:", int(peter_total))
    print("Crew:", int(crew_pay))
    print("RBF:", int(rbf))

if __name__ == "__main__":
    main()
