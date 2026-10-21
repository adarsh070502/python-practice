import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S QUIZ GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(r"C:\Users\Adarsh\PycharmProjects\Pandas\US_states_quiz_game\50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50",
                              prompt="Whats another state name?").title()

    if answer == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        data = pandas.DataFrame(states_to_learn)
        data.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.color("black")
        t.penup()
        t.hideturtle()
        state_data = data[data["state"] == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)


