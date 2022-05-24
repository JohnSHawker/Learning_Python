def main():
    number_of_space_pirates = int(input("\nHow many Raveger space pirates are there including Yondu and Peter?  > "))
    if number_of_space_pirates < 3:
        print("\nNot enough crew.")
        wait = input("\nPress Enter to continue\n")
        quit()
    else:
        pass
    number_of_units_plundered = int(input("\nHow many plundered units did the Ravegers enter port with?  > "))
    while True:
        if number_of_space_pirates <= 0 or number_of_units_plundered <= 0:
            print("\nEnter only positive integers for number of Raveger's and number of Unit's")
            wait = input("\nPress Enter to continue\n")
        else:
            break
    number_of_pirates_going_out = number_of_space_pirates - 2
    number_of_units_to_go_out = number_of_pirates_going_out * 3
    everyone_gets_a_share = number_of_space_pirates * 3
    number_of_units_after_port_cut = number_of_units_plundered - number_of_units_to_go_out
    yondu_percent = number_of_units_after_port_cut // (1 / 0.13)
    quill_percent = (number_of_units_after_port_cut - yondu_percent) // (1 / 0.11)
    number_of_units_to_split_per_crew_member = (number_of_units_after_port_cut - yondu_percent - quill_percent) // number_of_space_pirates
    RBF = number_of_units_after_port_cut - yondu_percent - quill_percent - (number_of_units_to_split_per_crew_member * number_of_space_pirates)
    if number_of_units_plundered < everyone_gets_a_share:
        print("Not enough units.")
        wait = input("\nPress Enter to continue\n")
        quit()
    else:
        pass
    print("\nUnits given to crew for shore leave:", int(number_of_units_to_go_out), "units")
    print("\nYondu's 13% take after crew shore leave cut is:", int(yondu_percent), "units")
    print("\nQuill's 11% take after Yondu's take is:", int(quill_percent), "units")
    print("\nAll crew members including Yondu and Quill get:", int(number_of_units_to_split_per_crew_member), "units each after all previous takes")
    print("\nYondu's total take is:", int(yondu_percent + number_of_units_to_split_per_crew_member), "units")
    print("\nQuill's total take is:", int(quill_percent + number_of_units_to_split_per_crew_member), "units")
    print("\nThe remainder of funds after equal crew spilt will go into the Raveger's Benevolent Fund, it will receive", int(RBF), "units.\n")
main()