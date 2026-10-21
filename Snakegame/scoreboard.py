from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Ariel", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.highscore =self.score
        self.score = 0
        self.update()
