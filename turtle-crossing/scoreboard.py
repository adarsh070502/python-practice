FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.level = 0
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-20,0)
        self.write(f"Game Over", font=FONT)
