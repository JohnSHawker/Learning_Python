# '''
# Project Name: Turtle Patterns 2
# Author: John Hawker
# Due Date: 2022-08-08
# Course: CS1400-X01

# This program will draw 3 different shapes in 3 different colors. Users can determine the height
# and width of the window. I learnded how to put functions into a program and call them later in
# the program.
# '''
# import turtle

# def triangle(size, color):
#     for _ in range(3):
#         my_turtle.fillcolor(color)
#         my_turtle.begin_fill()
#         my_turtle.forward(size)
#         my_turtle.lt(120)
#         my_turtle.end_fill()

# def square(size, color):
#     for _ in range(4):
#         my_turtle.fillcolor(color)
#         my_turtle.begin_fill()
#         my_turtle.forward(size)
#         my_turtle.rt(90)
#         my_turtle.end_fill()

# def circle(size, color):
#     my_turtle.fillcolor(color)
#     my_turtle.begin_fill()
#     my_turtle.circle(size)
#     my_turtle.end_fill()

# def main():
#     '''
#     Program starts here.
#     '''
#     try:
#         width = int(input("Width"))
#         height = int(input("Height"))
        
        
#     except ValueError:
#         print('Width and height must be positive integers.')
#         return

#     if width < 1 or height < 1:
#         print('Width and height must be positive integers.')
#         return

#     turtle.screensize(canvwidth = width, canvheight = height)
#     triangle(60, "red")
#     square(120, "yellow")
#     circle(240, "blue")

# if __name__ == "__main__":
#     my_turtle = turtle.Turtle()
#     main()
# turtle.mainloop()

import turtle
import sys

def square(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.lt(90)
        t.forward(height)
        t.lt(90)
    t.end_fill()

def triangle(length, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(length)
        t.lt(120)
    t.end_fill()

def circle(size, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

def house(scale):
    square((100 * scale), (100 * scale), "red")
    t.penup()
    t.goto(0, (100 * scale))
    t.pendown()
    triangle((100 * scale), "brown")
    t.penup()
    t.goto(0,0)
    t.goto((150 * scale),(150 * scale))
    t.pendown()
    circle((100 * scale), "yellow")

def main():

    try:
        scale = float(input("Scale "))

    except ValueError:
        print('Scale must be a positive integer.')
        return

    house(float(sys.argv[1]))

if __name__ == "__main__":
    t = turtle.Turtle()
    main()
turtle.mainloop()