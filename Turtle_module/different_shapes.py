from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("dark slate blue")

turtle_colors = ["azure", "dodger blue", "green yellow", "dark green", "firebrick", "crimson", "yellow", "rosy brown"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for j in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(angle)


for i in range(3, 11):
    timmy_the_turtle.color(random.choice(turtle_colors))
    draw_shape(i)

screen = Screen()
screen.exitonclick()
