from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.score = 0
        self.player_score()

    def player_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT, align="center", )

    def increase_score(self):
        self.score += 1
        self.player_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
