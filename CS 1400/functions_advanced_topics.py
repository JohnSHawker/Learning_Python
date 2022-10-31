# """Definitions seperated. Using **2 for squared"""
# import math

# def radius(x1, y1, x2, y2):
#     """Distance formula to determine the radius of a circle"""
#     return(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
  
# def area(x1, y1, x2, y2):
#     """Area of a circle function"""
#     return(math.pi * radius(x1, y1, x2, y2)**2)

# print(area(0, 0, 4, 4))

#---------------

# """Definitions seperated. using math.pow() to square"""
# import math

# def radius (x1, y1, x2, y2):
#     # using pythagorean theorem to determine radius, use x2 - x1 to determine length of x, use y2 - y1 to determine length of y
#     return(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))

# def area (x1, y1, x2, y2):
#     # using area formula for a circle by using center point and a point on the circle
#     return(math.pi * math.pow(radius(x1, y1, x2, y2), 2))

# print(area(0, 0, 4, 4))

#---------------

"""Definitions nested"""
import math

def area(x1, y1, x2, y2):
    def radius(x1, y1, x2, y2):
        return(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))
    return(math.pi * math.pow(radius(x1, y1, x2, y2), 2))

print(area(0, 0, 4, 4))