from turtle import Turtle,Screen
import random

screen = Screen()

is_race_on=False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win : ")
colors = ["red", "blue", "orange", "yellow", "green", "purple"]
y_poisition=[-70,-40,-10,20,50,80]
all_turtles=[]

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_poisition[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color=turtle.pencolor()
            if(user_bet == winning_color):
                print(f"YOU WON!! The {user_bet} turtle is the winner.")
            else:
                print(f"You have lost, The {winning_color} turtle is the winner.")
        randnum = random.randint(0, 10)
        turtle.forward(randnum)

screen.exitonclick()