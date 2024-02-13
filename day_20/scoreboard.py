from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.write_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 250)
        self.write_score()

    def write_score(self):
        super().write(f"Score: {self.score}", True, "center", ("Arial", 24, "normal"))
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, "center", ("Arial", 24, "normal"))
