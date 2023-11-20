from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)


def create_turtle(color, x_pos, y_pos):
    turtle = Turtle()
    turtle.penup()
    turtle.color(color)
    turtle.shape("turtle")
    turtle.setpos(x_pos, y_pos)
    return turtle


def move_turtle(turtle):
    number = round(random.randint(0, 10))
    turtle.forward(number)
    return


def is_winner(turtle):
    return turtle.xcor() >= 200


def initialize_turtles():
    turtle_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    turtles = []
    starting_x_pos = -240
    starting_y_pos = -100
    for color in turtle_colors:
        turtle = create_turtle(color=color, x_pos=starting_x_pos, y_pos=starting_y_pos)
        turtles.append(turtle)
        starting_y_pos += 40
    return turtles


def start_race():
    turtle_chosen = screen.textinput(
        title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
    )
    print(f"You bet: {turtle_chosen} turtle.")
    global winner
    turtles = initialize_turtles()
    continue_race = True
    while continue_race:
        index = 0
        while index < len(turtles):
            turtle = turtles[index]
            move_turtle(turtle)
            if is_winner(turtle):
                continue_race = False
                winner = turtle.color()[0]
                index = len(turtles)
                break
            index += 1
    if turtle_chosen == winner:
        print(f"You win! The {winner} turtle is the winner!")
    else:
        print(f"You lose! The {winner} turtle is the winner!")
    return


start_race()
screen.exitonclick()
