from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_clockwise():
    turtle.right(10)


def turn_counter_clockwise():
    turtle.left(10)


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_clockwise, "d")
screen.onkey(turn_counter_clockwise, "a")
screen.onkey(turtle.clear, "c")

screen.exitonclick()


