from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.color("blue")


def move_forward():
    my_turtle.forward(25)


def move_backward():
    my_turtle.back(25)


def move_right():
    my_turtle.right(25)


def move_left():
    my_turtle.left(25)


def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
