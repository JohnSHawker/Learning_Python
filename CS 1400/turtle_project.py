'''
Project Name: Turtle Patterns 1
Author: John Hawker
Due Date: 2022-06-10
Course: CS1400-X01

This program will draw 3 different shapes in 3 different colors. Users can determine the height
and width of the window. I learnded how to put functions into a program and call them later in
the program.
'''
import turtle

def triangle(size, color):
    for _ in range(3):
        my_turtle.fillcolor(color)
        my_turtle.begin_fill()
        my_turtle.forward(size)
        my_turtle.lt(120)
        my_turtle.end_fill()

def square(size, color):
    for _ in range(4):
        my_turtle.fillcolor(color)
        my_turtle.begin_fill()
        my_turtle.forward(size)
        my_turtle.rt(90)
        my_turtle.end_fill()

def circle(size, color):
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    my_turtle.circle(size)
    my_turtle.end_fill()

def main():
    '''
    Program starts here.
    '''
    try:
        width = int(input("Width"))
        height = int(input("Height"))
        
        
    except ValueError:
        print('Width and height must be positive integers.')
        return

    if width < 1 or height < 1:
        print('Width and height must be positive integers.')
        return

    turtle.screensize(canvwidth = width, canvheight = height)
    triangle(60, "red")
    square(120, "yellow")
    circle(240, "blue")

if __name__ == "__main__":
    my_turtle = turtle.Turtle()
    main()
turtle.mainloop()