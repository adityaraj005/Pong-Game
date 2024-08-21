from turtle import Turtle


class Dash:

    def __init__(self):
        lines = Turtle()
        lines.shape("square")
        lines.pensize(3)
        lines.color("white")
        lines.goto(x=0, y=290)
        lines.goto(x=0, y=-280)
        lines.hideturtle()
