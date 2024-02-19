from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            high_score = data.read()
            self.high_score = int(high_score)
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.write_score()

    def update_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.goto(0, 250)
        self.clear()
        super().write(f"Score: {self.score} High Score: {self.high_score}", True, "center", ("Arial", 24, "normal"))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
            
    def update_high_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))
