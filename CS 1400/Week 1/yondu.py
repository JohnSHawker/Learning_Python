'''
Project Name: yondu.py
Author: John Hawker
Due Date: 05/22/2022
Course: CS1400-X01

This program will calulate the cuts every reaver will get based off of the number of reavers and the number of units.
'''

def main():
    '''
    Program starts here.
    '''
    try:
        # (1) replace pass with your code
        reavers = int(input("How many reavers are there incuding Yondu and Peter?"))
        units = int(input("How many units did they come into port with?"))

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
    number_of_pirates_going_out = reavers - 2
    number_of_units_to_go_out = number_of_pirates_going_out * 3
    number_of_units_after_port_cut = units - number_of_units_to_go_out
    yondu_percent = number_of_units_after_port_cut // (1 / 0.13)
    quill_percent = (number_of_units_after_port_cut - yondu_percent) // (1 / 0.11)
    number_of_units_to_split_per_crew_member = (number_of_units_after_port_cut - yondu_percent - quill_percent) // reavers
    rbf = number_of_units_after_port_cut - yondu_percent - quill_percent - (number_of_units_to_split_per_crew_member * reavers)
    
    print("Yondu's share: ", int(yondu_percent + number_of_units_to_split_per_crew_member))
    print("Peter's share: ", int(quill_percent + number_of_units_to_split_per_crew_member))
    print("Crew: ", int(number_of_units_to_split_per_crew_member))
    print("RBF: ", int(rbf))

if __name__ == "__main__":
    main()
