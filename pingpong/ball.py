from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.x *= -1
        self.move_speed=0.1
