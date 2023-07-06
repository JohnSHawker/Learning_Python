import turtle

def rectangle(width, height):
    turtle.speed(0)
    for i in range(2):
        turtle.forward(width)
        turtle.lt(90)
        turtle.forward(height)
        turtle.lt(90)

def triangle(length):
    turtle.speed(0)
    for i in range(3):
        turtle.lt(120)
        turtle.forward(length)

def move_turtle(x, y):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()

rectangle(100, 100)
move_turtle(100, 100)
triangle(100)
move_turtle(40, 0)
rectangle(20, 40)
move_turtle(10, 50)
rectangle(20, 20)
move_turtle(70, 50)
rectangle(20, 20)

turtle.mainloop()
