from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__
        self.score = 0

    def increase_score(self):
        self.score += 1

    def game_over(self):
        game = Turtle()
        game.penup()
        game.color("black")
        game.hideturtle()
        game.setpos(-300, 0)
        game.write(
            "Congratulations! You have named all 50 states!",
            move=False,
            align="left",
            font=("Sans Serif", 16, "normal"),
        )
