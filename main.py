import turtle
import pandas
from state import State


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

correct_answers_list = []
guess_counter = 0

while guess_counter != 50:
    answer_state = screen.textinput(title=f"{guess_counter}/50 Guess the State", prompt="What's another name of the "
                                                                                        "State").title()
    if answer_state == "Exit":
        break

    if answer_state in states:
        guess_counter += 1
        guessed_state = State(answer_state)
        cord = data[data.state == answer_state]
        x = int(cord["x"])
        y = int(cord["y"])
        guessed_state.move_state(x, y)
        states.remove(answer_state)
        correct_answers_list.append(answer_state)

learn_dict = {
    "States": states
}

new_data = pandas.DataFrame(learn_dict)
new_data.to_csv("States to learn, loser")


