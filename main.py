import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


def write_state(state_txt):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == state_txt]
    t.goto(x=int(state_data.x), y=int(state_data.y))
    # t.write(state_data.state.item())
    t.write(state_txt)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Key in the state's name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                write_state(state)
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        write_state(answer_state)

turtle.mainloop()
