from turtle import Screen
from paddle import Paddle1, Paddle2
from ball import Ball
from dash import Dash
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Welcome to Pong Game!")
screen.tracer(0)

Lines = Dash()
paddle_r = Paddle1()
paddle_l = Paddle2()
Score = Scoreboard()
ball = Ball()

screen.listen()
screen.onkeypress(paddle_r.go_up_1, "Up")
screen.onkeypress(paddle_l.go_up_2, "w")
screen.onkeypress(paddle_l.go_down_2, "s")
screen.onkeypress(paddle_r.go_down_1, "Down")

time_stamp = 0.1
game_is_on = True
while game_is_on:
    time.sleep(time_stamp)  # This will pause the loop for 0.05 seconds between each iteration
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        time_stamp /= 1.2
        time.sleep(time_stamp)
    if ball.xcor() > 390:
        Score.increase_score_l()
        time.sleep(2)
        time_stamp = 0.1
        ball.refresh()

        if Score.current_score_l == 10:
            Score.game_over_l()
            game_is_on = False

    elif ball.xcor() < -390:
        Score.increase_score_r()
        time.sleep(2)
        time_stamp = 0.1
        ball.refresh()

        if Score.current_score_r == 10:
            Score.game_over_r()
            game_is_on = False


screen.exitonclick()
