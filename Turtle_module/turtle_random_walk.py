from turtle import Turtle, Screen
import random

turtle_colors = ["azure", "dodger blue", "green yellow", "dark green", "firebrick",
                 "crimson", "yellow", "rosy brown"]
directions = [0, 90, 180, 270]
timy_turtle = Turtle()
timy_turtle.width(10)
timy_turtle.speed(10)

for i in range(200):
    timy_turtle.color(random.choice(turtle_colors))
    timy_turtle.forward(25)
    timy_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

