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
turtle.done()