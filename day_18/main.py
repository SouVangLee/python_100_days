import colorgram
import random
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


extracted_colors = colorgram.extract("image.jpg", 15)
colors_list = []

for color in extracted_colors:
    colors_list.append(color.rgb)
colors_list = tuple(colors_list)


def random_color():
    index = round(random.randint(0, len(colors_list) - 1))
    return colors_list[index]

def hirst_painting(dots_per_line=6, num_of_rows=10, space_between_rows=50, dot_size=25):
    screen.colormode(255)
    turtle.penup()
    turtle.setpos(-250, -250)
    
    for row in range(0, num_of_rows):
        current_y_pos = turtle.ycor()
        if row > 0:
            current_y_pos += space_between_rows
            turtle.setpos(-250, current_y_pos)
        turtle.pendown()
        for _ in range(0, dots_per_line):
            color = random_color()
            turtle.dot(dot_size, color)
            turtle.penup()
            turtle.forward(50)


hirst_painting(6, 6, 50, 25)
# turtle.dot(25, "red")

screen.exitonclick()
