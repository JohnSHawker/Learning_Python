'''
A program that divides wages up evenly among a work crew. The manager gets 13%,
The supervisor gets 11%, and each remaining crew member gets 3 units ($2.33 value per unit)
bonus. After the remainder is divided up evenly among all crew members including management,
if there is any remainder then it is put into a charity fund.
The user inputs the wage amount as an interger and how many members of the crew there are, if 
the user inputs less than 3 work crew the program needs to quit.
'''
# Import math for the math.floor() function to round down to the next full integer
import math


def main():
    print('Time to calculate that booty!')
    reavers = int(input('How many reavers are there including Yondu and Peter in total? '))
    reaver_amount(reavers)
    units = int(input('How many units did the reavers come to port with? '))
    yondus = yondu_cut(units)
    peters = peter_cut(units)
    crew_leave = shore_leave(reavers)
    # print statement used for debugging only
    print(int(yondus))
    print(int(peters))
    print(int(crew_leave))
    
  
def reaver_amount(reavers):
    '''Checks to make sure that 
    there are more than 3 reavers
    '''  

    if reavers < 3:
        print('You do not have enough reavers.')
        quit()
    else:
        return reavers

def yondu_cut(total):
    '''Calculates the total amount 
    Yondu gets before splitting the shares
    among the group of reavers.
    '''
    yondus = total * 0.13
    return yondus

def peter_cut(total):
    '''Calculates the total amount
    Peter gets before splitting the shares 
    among the group og reavers
    '''
    peters = total * 0.11
    return peters

def shore_leave(crew):
    '''Calculates the amount
    the remaining crew "spends" on 
    shore leave, or the 3 units per crew
    excluding Yondu and Peter.
    '''
    crew_leave = (crew - 2) * 3
    return crew_leave


'''The below code can be ignored as it was notes on how to
do the math required for the problem overall. 
I will later incorporate all of the math over multiple variables.
The below calculations are also broken....yay
'''    
#     calculate()

# def calculate():
#     shore_leave = crew - 2
#     bonus = shore_leave * 3
#     yondu =  booty * 0.13
#     peter_bonus = booty * 0.11
#     # total = booty - int(yondu)
#     # total = booty - peter_bonus
#     # total = booty - bonus
#     total=int(booty) - int(yondu) - int(peter_bonus) - int(bonus)
#     print(total)
#     shares = total / crew
#     shares = math.floor(shares)

#     yondu_total = yondu + shares
#     peter_total = peter_bonus + shares
#     print(peter_total)
#     print(f"Yondu's share: {yondu_total}")
#     print(bonus)

if __name__ == '__main__':
    main()