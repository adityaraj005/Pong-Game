from turtle import Turtle

Y_COR = 231


class Paddle1(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        # turtle_1.shapesize(stretch_wid=20, stretch_len=100)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(x=350, y=50)

    def go_up_1(self):
        new_y = self.ycor() + 20
        if self.ycor() < Y_COR:
            self.goto(self.xcor(), new_y)

    def go_down_1(self):
        new_y = self.ycor() - 20
        if self.ycor() > -Y_COR:
            self.speed("fast")
            self.goto(self.xcor(), new_y)


class Paddle2(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        # turtle_1.shapesize(stretch_wid=20, stretch_len=100)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(x=-350, y=50)

    def go_up_2(self):
        new_y = self.ycor() + 20
        if self.ycor() < Y_COR:
            self.goto(self.xcor(), new_y)

    def go_down_2(self):
        new_y = self.ycor() - 20
        if self.ycor() > -Y_COR:
            self.speed("fast")
            self.goto(self.xcor(), new_y)
