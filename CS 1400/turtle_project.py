'''
Project Name:
Author:
Due Date: YYYY-MM-DD
Course: CS1400-zzz

Put your description here, lessons learned here, and any other information
someone using your program would need to know to make it run.
'''
import turtle

# (3) add functions here that your main program calls
# to do stuff.
def triangle(size):
    for _ in range(3):
        my_turtle.forward(size)
        my_turtle.lt(120)

def main():
    '''
    Program starts here.
    '''
    # try:
    #     pass
    #     # TODO user input for window size
    # except ValueError:
    #     print('Width and height must be positive integers.')
    #     return

    # if width < 1 or height < 1:
    #     print('Width and height must be positive integers.')
    #     return

    # (2) replace pass with your code
    # TODO call functions for shapes here
    triangle(60)
if __name__ == "__main__":
    my_turtle = turtle.Turtle()
    main()
    turtle.mainloop()