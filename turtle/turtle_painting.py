import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


circles = 0
while circles <= 360:
    timmy.pencolor(random_color())
    timmy.setheading(circles)
    timmy.circle(50, None, None)
    circles += 20

screen = t.Screen()
screen.exitonclick()
