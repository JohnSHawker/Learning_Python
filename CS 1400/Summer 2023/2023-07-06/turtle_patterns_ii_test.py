import turtle

def square(length, scale):
    turtle.pendown()
    turtle.pencolor('red')
    length = length * scale
    for _ in range(4):
        turtle.fd(length)
        turtle.lt(90)
    turtle.penup()


def triangle(length, scale):
    turtle.pendown()
    turtle.pencolor('yellow')
    length = length * scale
    for _ in range(3):
        turtle.fd(length)
        turtle.lt(120)
    turtle.penup()

def circle(length, scale):
    turtle.pendown()
    turtle.pencolor('blue')
    length = length * scale
    for _ in range(360):
        turtle.fd(length)
        turtle.lt(1)
    turtle.penup()

def draw(width, height, scale, tilt):
    turtle.screensize(canvwidth = width, canvheight = height)
    turtle.speed(0)
    house(scale, tilt)
    house(scale / 2, tilt)
    # square(scale)
    # turtle.fd(100 * scale)
    # triangle(scale)
    # turtle.fd(100 * scale)
    # circle(scale)

def house(scale, tilt):
    turtle.setheading(tilt)
    turtle.penup()
    turtle.goto(0,0)
    square(100, scale)
    turtle.fd(40 * scale)
    square(20, scale)
    turtle.goto(0,0)
    turtle.fd(20 * scale)
    turtle.lt(90)
    turtle.fd(40 * scale)
    turtle.rt(90)
    square(20, scale)
    turtle.goto(0,0)
    turtle.fd(80 * scale)
    turtle.lt(90)
    turtle.fd(40 * scale)
    square(20, scale)
    turtle.goto(0,0)
    turtle.fd(100 * scale)
    turtle.rt(90)
    triangle(100, scale)


draw(100,100, 2, 30)
turtle.mainloop()