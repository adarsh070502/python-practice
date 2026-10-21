from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time

from Snakegame.snake import Snake

screen = Screen()
screen.setup(width=600, height=600)  # to set screen width and hieght
screen.bgcolor("black")    # to set screen color
screen.title("My snake Game")          # to set screen title
screen.tracer(0)  # animation off    # to turn off animation

snake = Snake()       # object of Snake class
food = Food()           # object of Snake class
scoreboard = ScoreBoard()       # object of Snake class

screen.listen()
screen.onkey(snake.up, "Up")              #when arrow up is pressed snake.up method will be called
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()  # (related to tracer method, updates the screen only after all pieces of snake are moved      #updates screen
    time.sleep(0.1)   # sleep the screen for 0.1
    snake.move()   # move is a method in Snake clss to move the snake

    #detecting collisoion with food
    if snake.head.distance(food) < 15:   #distance method checks distance between two turtles and returns distance b/w two tutrtles
        food.refresh()                    # randomizes the food on screen
        snake.extra_segment()              # adds an extra segment when food is hit
        scoreboard.increase_score()       #increases the score on the screen

    #detect collison with walls
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
