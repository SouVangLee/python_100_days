from turtle import Turtle, Screen
import random
import time

SNAKE_SIZE = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake!")
# turn off animation
screen.tracer(0)


def add_segment(x_pos, y_pos):
    segment = Turtle("square")
    segment.penup()
    segment.color(random.choice(["white", "blue", "orange", "yellow", "grey", "red"]))
    segment.setpos(x_pos, y_pos)
    return segment


def snake_head_starting_pos():
    starting_x_pos = random.randint(-12, 12) * 20
    starting_y_pos = random.randint(-12, 12) * 20
    snake_head = Turtle("square")
    snake_head.penup()
    snake_head.color("green")
    snake_head.setpos(starting_x_pos, starting_y_pos)
    return snake_head


def snake_body_starting_pos(head):
    starting_x_pos, starting_y_pos = head.pos()
    body_add_x_pos = starting_x_pos + SNAKE_SIZE
    body_subtract_x_pos = starting_x_pos - SNAKE_SIZE
    body_add_y_pos = starting_y_pos + SNAKE_SIZE
    body_subtract_y_pos = starting_y_pos - SNAKE_SIZE

    body_pos_list = [
        (body_add_x_pos, starting_y_pos),
        (body_subtract_x_pos, starting_y_pos),
        (starting_x_pos, body_add_y_pos),
        (starting_x_pos, body_subtract_y_pos),
    ]
    body_x_pos, body_y_pos = random.choice(body_pos_list)
    return add_segment(body_x_pos, body_y_pos)


def get_new_segment_pos(current_tail, previous_tail):
    current_x, current_y = current_tail
    previous_x, previous_y = previous_tail
    if previous_x == current_x:
        if previous_y < current_y:
            return (current_x, current_y + SNAKE_SIZE)
        return (current_x, current_y - SNAKE_SIZE)
    else:
        if previous_x < current_x:
            return (current_x + SNAKE_SIZE, current_y)
        return (current_x - SNAKE_SIZE, current_y)


def initialize_snake():
    snake = []
    head = snake_head_starting_pos()
    body = snake_body_starting_pos(head)

    tail_x_pos, tail_y_pos = get_new_segment_pos(
        current_tail=body.pos(), previous_tail=head.pos()
    )
    tail = add_segment(tail_x_pos, tail_y_pos)

    snake.append(head)
    snake.append(body)
    snake.append(tail)
    return snake


def get_current_direction():
    global snake
    head_x, head_y = snake[0].pos()
    previous_head_x, previous_head_y = snake[1].pos()

    if previous_head_x == head_x:
        if head_y > previous_head_y:
            return "Up"
        else:
            return "Down"
    else:
        if head_x > previous_head_x:
            return "Right"
        else:
            return "Left"


def set_initial_movement():
    global snake
    global current_direction
    for segment in snake:
        if current_direction == "Up":
            segment.left(90)
        elif current_direction == "Down":
            segment.right(90)
        elif current_direction == "Left":
            segment.right(180)


def turn_snake_up():
    global snake
    global current_direction
    print(f"current direction: {current_direction}")
    head = snake[0]
    previous_pos = head.pos()
    current_head_x_pos, current_head_y_pos = previous_pos
    if current_direction == "Left" or current_direction != "Right":
        new_y_pos = current_head_y_pos + 20
        head.setpos(current_head_x_pos, new_y_pos)

    current_pos = ()
    for index in range(1, len(snake)):
        segment = snake[index]
        current_pos = snake[1].pos()
        segment.setpos(previous_pos)
        previous_pos = current_pos
    current_direction = "Up"


snake = initialize_snake()
current_direction = get_current_direction()
set_initial_movement()
screen.listen()
screen.update()
screen.onkey(turn_snake_up(), "Up")
game_is_on = True
i = 100
while i > 0:
    # time.sleep(1)
    screen.update()
    for index in range(len(snake) - 1, 0, -1):
        segment = snake[index]
        next_segment = snake[index - 1]
        segment.setpos(next_segment.pos())
        time.sleep(0.5)

    snake[0].forward(20)


screen.exitonclick()
