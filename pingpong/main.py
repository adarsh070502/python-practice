import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from pingpong.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, key="Up")
screen.onkeypress(r_paddle.go_down, key="Down")
screen.onkeypress(l_paddle.go_up, key="w")
screen.onkeypress(l_paddle.go_down, key="s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()   # ball moves continously

    # detection with walls
    if ball.ycor() > 280 or ball.ycor() < -280:  #ball hits top or bootom walls it bounces
        ball.bounce_y()

    # detection with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x() #if the distance between paddle and ball is less than 50 and the ball crosses 320 pixels in xcor it bounces

    #to detect rpaddle misses
    if ball.xcor() > 380:  # if the ball crosses the 380 picxel in xcor lpaddle wins
        ball.reset_position()
        scoreboard.l_update()

    # to detect lpaddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_update()

screen.exitonclick()
