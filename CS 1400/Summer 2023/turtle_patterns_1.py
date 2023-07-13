'''
Project Name: Turtle Patterns 1
Author: John Hawker
Due Date: 2023-06-08
Course: CS1400-X02

User should be asked to input values for the window height and width.
The turtle window should open to the specified size and draw the atomic shapes.
'''
import turtle

def triangle(size, color):
    for _ in range(3):
        my_turtle.fillcolor(color)
        my_turtle.begin_fill()
        my_turtle.fd(size)
        my_turtle.lt(120)
        my_turtle.end_fill()

def square(size, color):
    for _ in range(4):
        my_turtle.fillcolor(color)
        my_turtle.begin_fill()
        my_turtle.fd(size)
        my_turtle.rt(90)
        my_turtle.end_fill()

def circle(size, color):
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    my_turtle.circle(size)
    my_turtle.end_fill()


# (3) add functions here that your main program calls
# to do stuff.

def get_dimensions():
    width = input("Window width > ")
    height = input("Window height > ")
    return width, height



def draw(width, height):
    '''
    Sets the size of the screen to width and height and draws a doodle.
    '''
    # (2) replace pass with your code
    pass
