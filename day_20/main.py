from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

SNAKE_SIZE = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake!")
# turn off animation by setting tracer to 0
# screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
    
game_is_on = True
while game_is_on:
    screen.update()
    # time.sleep(.1)
    
    snake.move()
    
    # Detect collision with  food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect wall collision
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if(x_cor > 280 or x_cor < -280 or y_cor > 280 or y_cor < -280):
        game_is_on = False
        scoreboard.game_over()
    
    # Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
        

screen.exitonclick()