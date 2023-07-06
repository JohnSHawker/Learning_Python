import turtle

turtle.speed(0)

# Draw a rectangle with width 100 and height 100
for i in range(2):
    turtle.forward(100)
    turtle.lt(90)
    turtle.forward(100)
    turtle.lt(90)

# Move the turtle to (100, 100) to start the roof
turtle.penup()
turtle.goto(100, 100)
turtle.setheading(0)
turtle.pendown()

# Draw a triangle with sides of length 100
for i in range(3):
    turtle.lt(120)
    turtle.forward(100)

# Move the turtle to (40, 0) to start the door
turtle.penup()
turtle.goto(40, 0)
turtle.setheading(0)
turtle.pendown()

# Draw a rectangle with width 20 and height 40
for i in range(2):
    turtle.forward(20)
    turtle.lt(90)
    turtle.forward(40)
    turtle.lt(90)

# Move the turtle to (10, 50) to start the left window
turtle.penup()
turtle.goto(10, 50)
turtle.setheading(0)
turtle.pendown()

# Draw a rectangle with width 20 and height 20
for i in range(2):
    turtle.forward(20)
    turtle.lt(90)
    turtle.forward(20)
    turtle.lt(90)

# Move the turtle to (70, 50) to start the right window
turtle.penup()
turtle.goto(70, 50)
turtle.setheading(0)
turtle.pendown()

# Draw a rectangle with width 20 and height 20
for i in range(2):
    turtle.forward(20)
    turtle.lt(90)
    turtle.forward(20)
    turtle.lt(90)

turtle.mainloop()

# import turtle

# def rectangle(width, height):
#     turtle.speed(0)
#     for i in range(2):
#         turtle.forward(width)
#         turtle.lt(90)
#         turtle.forward(height)
#         turtle.lt(90)

# def triangle(length):
#     turtle.speed(0)
#     for i in range(3):
#         turtle.lt(120)
#         turtle.forward(length)

# def move_turtle(x, y):
#     turtle.speed(0)
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.setheading(0)
#     turtle.pendown()

# rectangle(100, 100)
# move_turtle(100, 100)
# triangle(100)
# move_turtle(40, 0)
# rectangle(20, 40)
# move_turtle(10, 50)
# rectangle(20, 20)
# move_turtle(70, 50)
# rectangle(20, 20)

# turtle.mainloop()
