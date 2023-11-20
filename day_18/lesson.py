from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()


def draw_shapes(num_of_sides):
    for number_of_sides in range(3, num_of_sides):
        r = round(random.randint(0, 255))
        g = round(random.randint(0, 255))
        b = round(random.randint(0, 255))
        angle = 360 / number_of_sides

        screen.colormode(255)
        turtle.pencolor(r, g, b)
        for _ in range(number_of_sides):
            turtle.right(angle)
            turtle.forward(100)


def random_walk(num_of_steps):
    turtle.width(4)
    turtle.speed(10)
    for _ in range(num_of_steps):
        r = round(random.randint(0, 255))
        g = round(random.randint(0, 255))
        b = round(random.randint(0, 255))
        screen.colormode(255)
        turtle.pencolor(r, g, b)
        angles_list = [0, 90, 180, 270]
        index = round(random.randint(0, 3))
        angle = angles_list[index]
        turtle.setheading(angle)
        turtle.forward(25)


def spiro_graph(line_width=0, spacing=1):
    turtle.speed(0)
    turtle.width(line_width)
    for angle in range(0, 360, spacing):
        r = round(random.randint(0, 255))
        g = round(random.randint(0, 255))
        b = round(random.randint(0, 255))
        screen.colormode(255)
        turtle.pencolor(r, g, b)
        turtle.circle(100)
        turtle.setheading(angle)


# draw_shapes(11)
# random_walk(100)
spiro_graph()
screen.exitonclick()
