import random
import sys
import math

def pa(iterations, steps):
    north = 0
    south = 0
    east = 0
    west = 0
    
    for i in range(steps):
        direction = random.randint(1,4)
        if direction == 1:
            north += 1
        elif direction == 2:
            south += 1
        elif direction == 3:
            east += 1
        else:
            west += 1

    n_s_distance = (north - south)
    e_w_distance = (east - west)
    print(north)
    print(south)
    print(east)
    print(west)

pa(0, int(input("How many steps? ")))