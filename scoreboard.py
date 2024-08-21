from turtle import Turtle

ALIGNMENT = "center"
FONT_A = ("Arial", 50, "bold")
FONT_B = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score_l = 0
        self.current_score_r = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=-3, y=230)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"{self.current_score_l}   {self.current_score_r}", move=False, align=ALIGNMENT, font=FONT_A)

    def increase_score_l(self):
        self.current_score_l += 1
        self.update()

    def increase_score_r(self):
        self.current_score_r += 1
        self.update()

    def game_over_l(self):
        self.goto(-10, 10)
        self.write(arg="GAME   OVER", align=ALIGNMENT, font=FONT_B)

    def game_over_r(self):
        self.goto(-10, 10)
        self.write(arg="GAME   OVER", align=ALIGNMENT, font=FONT_B)
