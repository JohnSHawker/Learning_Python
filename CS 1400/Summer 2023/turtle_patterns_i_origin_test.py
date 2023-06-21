'''
Project Name: Turtle Patterns I
Author: John Hawker
Due Date: 2023-06-08
Course: CS1400-X02

User should be asked to input values for the window height and width.
If the user input is not an int then there should be a ValueError.
If the user input is not a value > 1 for width or height then there should be an error.
The turtle window should open to the specified size and draw the atomic shapes.
'''
import turtle

def square():
    turtle.pencolor('red')
    for _ in range(4):
        turtle.fd(50)
        turtle.lt(90)
    turtle.penup()
    turtle.fd(100)
    turtle.pendown()
  
def triangle():
    turtle.pencolor('yellow')
    for i in range(3):
        turtle.fd(57.73502692)
        turtle.lt(120)
    turtle.penup()
    turtle.fd(127)
    turtle.pendown()

def circle():
    turtle.pencolor('blue')
    for i in range(360):
        turtle.fd(0.45)
        turtle.lt(1)

def get_dimensions():
    try:
        width = int(input("width "))
        height = int(input("height "))
        
    except ValueError:
        print('Width and height must be positive integers.')
        return

    if width < 1 or height < 1:
        print('Width and height must be positive integers.')
        return
    
    return width, height

def draw(width, height):
    turtle.screensize(canvwidth = width, canvheight = height)
    square()
    triangle()    
    circle()
