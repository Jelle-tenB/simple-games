from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(cords)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if self.ycor() < 260:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -260:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
