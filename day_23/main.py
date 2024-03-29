import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    
    # Level up and reset player position
    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.add_level()
        player.reset_position()
        car_manager.increase_speed()

    # Detect collision with car
    for car in car_manager.car_list:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False
    
screen.exitonclick()
