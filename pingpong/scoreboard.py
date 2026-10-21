from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update()


    def update(self):
        self.clear()
        self.goto(x=-100, y=250)  # lscore
        self.write(arg=f"{self.l_score}", align="center", font=("Ariel", 24, "normal"))
        self.goto(x=100, y=250)  #rscore
        self.write(arg=f"{self.r_score}", align="center", font=("Ariel", 24, "normal"))

    def l_update(self):  # if rpaddle missess lscore gets updated
        self.l_score += 1
        self.update()

    def r_update(self):
        self.r_score += 1
        self.update()

