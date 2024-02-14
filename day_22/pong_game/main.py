from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

left_paddle = Paddle(x_pos=-350, y_pos=0)
right_paddle = Paddle(x_pos=350, y_pos=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect ball collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect ball collision with paddles
    if (
        ball.distance(right_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(left_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()
        
    # Detect if right_padding misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.add_left_point()
        
    # Detect if left_padding misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.add_right_point()

screen.exitonclick()
