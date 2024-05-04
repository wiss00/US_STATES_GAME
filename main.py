import turtle
import pandas

screen = turtle.Screen()
screen.title("us states")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
game_is_on = True
states_name = data["state"]

all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 guessed state", prompt="what's your answer?").title()
    if answer == "Exit":
        not_guessed=[state for state in all_states if state not in guessed_states]
        new_data=pandas.DataFrame(not_guessed)
        new_data.to_csv("states_to_learn2.csv")
        break
    if answer in all_states:
        guessed_states.append(answer)
        answer_ins = data[data.state == answer]
        x = int(answer_ins.x)
        y = int(answer_ins.y)

        t = turtle.Turtle()
        t.penup()
        t.goto(x, y)
        t.write(answer, font=("Arial", 10, "bold"), align="center")
        t.hideturtle()
