'''
A program that divides wages up evenly among a work crew. The manager(Yondu) gets 13%,
The supervisor(Peter) gets 11%, and each remaining crew member gets 3 units ($2.33 value per unit)
bonus. After the remainder is divided up evenly among all crew members including management,
if there is any remainder then it is put into a charity fund.
The user inputs the wage amount as an interger and how many members of the crew there are, if 
the user inputs less than 3 work crew the program needs to quit.
Author: Kameron Squire
'''
# Import math for the math.floor() function to round down to the next full integer
import math


def main():
    print('Welcome Yondu! This program is designed for you to \
calculate the total cut each crew member receives after a \
job WELL DONE! \nYou get to skim off the top, and Quill gets a little\
something because he is like a son to you....Everyone else \
screw em! \nBut also be the benevolent Captain that you are!')

    #Variables to calculate everyone's cut
    reavers = int(input('How many reavers are there including (Yours truly!)Yondu and Peter in total? '))
    reaver_amount(reavers)
    units = int(input('How many units did the reavers come to port with? '))
    check = unit_check(units, reavers)
    crew_leave = shore_leave(reavers)
    yondus = yondu_cut(units, crew_leave)
    peters = peter_cut(units, crew_leave, yondus)
    everyones_cut = crews_cut(reavers, units, yondus, peters, crew_leave)
    rbf = RBF(reavers, units, yondus, peters, crew_leave, everyones_cut)
    yondu_final = yondu_total(yondus, everyones_cut)
    peter_final = peter_total(peters, everyones_cut)

    #Dollar variables
    yon_dol = dollar_amount(yondu_final)
    peter_dollar = dollar_amount(peter_final)
    crew_cash = dollar_amount(everyones_cut)


    #Prints the result of the everyone's cut
    print('Yondu had the final amount of: ', yondu_final)
    print('Peter had the final amount of: ', peter_final)
    print(f'Crew: {everyones_cut}')
    print(f'RBF: {rbf}')
    print('')

    #For fun I added the US dollar earnings based off the .txt document
    print("Everyone's final cut based on the US dollar")
    print(f"Yondu's dollar amount: ${yon_dol:.2f}")
    print(f"Peter's dollar amount: ${peter_dollar:.2f}")
    print(f"Crew's dollar amount: ${crew_cash:.2f}")
  
def reaver_amount(reavers):
    '''Checks to make sure that 
    there are more than 3 reavers
    '''  

    if reavers <= 3:
        print('You do not have enough reavers.')
        quit()
    else:
        return int(reavers)

def yondu_cut(total, crew_leave):
    '''Calculates the total amount 
    Yondu gets before splitting the shares
    among the group of reavers.
    '''
    yondus = math.floor((total - crew_leave) * 0.13)
    return yondus

def peter_cut(total, crew_leave, yondus):
    '''Calculates the total amount
    Peter gets before splitting the shares 
    among the group og reavers
    '''
    peters = math.floor((total - crew_leave - yondus) * 0.11)
    return peters

def shore_leave(crew):
    '''Calculates the amount
    the remaining crew "spends" on 
    shore leave, or the 3 units per crew
    excluding Yondu and Peter.
    '''
    crew_leave = (crew - 2) * 3
    return crew_leave

def crews_cut(
    reavers, units, yondus, 
    peters, crew_leave):
    '''Calculates the amount each
    crew member receives from the job
    after the bonuses have been taken out.
    '''
    cut = (units - yondus - peters - crew_leave) // reavers
    return (cut)

def RBF(
    reavers, units, yondus, 
    peters, crew_leave, cut):
    '''Calculates the remainder amount that
    doesn't split evenly among the crew and 
    puts that remainder in the RBF fund(charity).
    '''
    rbf = math.ceil(units - yondus - peters - crew_leave - (cut * reavers))
    return (rbf)

def yondu_total(bonus, cut):
    '''Calculates Yondu's total amount
    by combining his cut with his bonus
    percentage.
    '''
    yondu_final = bonus + cut
    return yondu_final

def peter_total(bonus, cut):
    '''Calculates Peter's total amount
    by combining his cut with his bonus
    percentage.
    '''
    peter_final = bonus + cut
    return peter_final

def dollar_amount(units):
    '''Calculates US dollar amount
    of each individuals cut
    '''
    dollars = units * 2.33
    return dollars

def unit_check(units, reavers):
    '''Checks to make sure that units
    and reavers entered are a positive integer.
    Also checks to make sure there are enough
    units to divide among the crew.
    '''
    if units <= reavers * 3:
        print('Not enough units.')
        quit()
    else:
        pass


if __name__ == '__main__':
    main()