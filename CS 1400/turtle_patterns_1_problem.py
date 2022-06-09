# usefull turtle commands 
# bob.rt() == bob.right()
# bob.lt() == bob.left()

# import turtle

# t = turtle.Turtle()
# t.shape('turtle')
# t.pensize(2)

# for i in range(4):
#     t.forward(130)
#     for i in range (3):
#         t.rt(90)
#         t.forward(30)
# # All of your turtle commands
# # go in this space here.


# turtle.mainloop()      # should be last line of program

# for i in range(360):
#     t.forward(1)
#     t.rt(1)

# for i in range(30):
#     t.forward(i * 4)
#     t.rt(90)

import turtle

# turtle setup
bob = turtle.Turtle()
bob.color('black')
bob.pensize(5)
bob.shape('turtle')
bob.pencolor('yellow')

# square
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.right(90)

# move for second shape
bob.penup()
bob.forward(100)
bob.pendown()
bob.pencolor('red')

# triangle
bob.right(60)
bob.forward(115.4700538)
bob.left(120)
bob.forward(115.4700538)
bob.left(120)
bob.forward(115.4700538)

# move for last shape
bob.penup()
bob.forward(350)
bob.pendown()
bob.pencolor('blue')

# circle
bob.circle(50)

# make this your last line so that the window stays open until you close it
turtle.mainloop()