from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X_COOR = 340
OFF_X_COOR = -280


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:     
            y_coor = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(STARTING_X_COOR, y_coor)
            self.car_list.append(new_car)
    
    def move_cars(self):
        for car in self.car_list:
            car.backward(self.current_speed)
            
    def remove_car(self):
        self.car_list = self.car_list[1:]
        
    def increase_speed(self):
        self.current_speed += MOVE_INCREMENT
