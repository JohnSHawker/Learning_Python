'''
Project Name: Turtle Patterns I
Author: John Hawker
Due Date: 2023-06-08
Course: CS1400-X02

User should be asked to input values for the window height and width.
If the user input is not an int then there should be a ValueError.
If the user input is not a value > 1 for width or height then there 
should be an error.
The turtle window should open to the specified size and draw the atomic shapes.
The image should be saved as a .png file.
The turtle window should close.
The program should be complete.
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
    for _ in range(3):
        turtle.fd(57.73502692)
        turtle.lt(120)
    turtle.penup()
    turtle.fd(127)
    turtle.pendown()

def circle():
    turtle.pencolor('blue')
    for _ in range(360):
        turtle.fd(0.45)
        turtle.lt(1)

def get_dimensions():
    """
    To get the program to work when I press "TRY IT!" I have to use the code:
    
    width = int(input("width "))
    hight = int(input("height "))

    or

    width = input("width ")
    width = int(width)
    height = input("height ")
    height = int(height)

    But I get Input validation: Positive integers (6/10) in the "Check It!"
    autograder.

    If I use the code:

    width = input(int("width "))
    height = input(int("height "))

    I get Input validation: Positive integers (10/10) in the "Check It!"
    autograder.

    When I use the code:

    try:
        width = input('width ')
        width = int(width)
        height = input('height ')
        height = int(height)
        
    except ValueError:
        print('Width and height must be positive integers.')
        return

    if width < 1 or height < 1:
        print('Width and height must be positive integers.')
        return
    
    I get a the error:

        Traceback (most recent call last):
     File "run_doodles.py", line 84, in <module>
        main()
     File "run_doodles.py", line 72, in main
        (width, height) = doodles.get_dimensions()
    TypeError: 'NoneType' object is not iterable

    It was my understanding that we needed to make sure the value was an int and
    a positive interger. It looks like that is taken care of in run_doodle.py. I
    left all of this code here to show what I have tried to make this code work
    correctly. Please let me know If I should have coded this project a different
    way.
    """
    
    # width = input("width")
    # width = int(width)
    # height = input("height")
    # height = int(height)
    
    # width = input(int("width"))
    # height = input(int("height"))
    
    # try:
    # width = input('width ')
    # width = int(width)
    # height = input('height ')
    # height = int(height)
        
    # except ValueError:
    #     print('Width and height must be positive integers.')
    #     return

    # if width < 1 or height < 1:
    #     print('Width and height must be positive integers.')
    #     return
    
    width = int(input('width '))
    height = int(input('height '))
    return (width, height)

def draw(width, height):
    turtle.screensize(canvwidth = width, canvheight = height)
    square()
    triangle()    
    circle()

draw(100,100)