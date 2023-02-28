import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.penup()
t.hideturtle()
# game_on = True
# score = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f"Guess State {len(guessed_states)}/50", prompt="What is another state?")).title()

    data = pd.read_csv("50_states.csv")

    state_name_list = data.state.tolist()
    for x in state_name_list:
        if answer_state.lower() == x.lower():
            x_cor = (data[(data.state) == answer_state]).loc[:, "x"]
            y_cor = (data[(data.state) == answer_state]).loc[:, "y"]
            t.goto(int(x_cor), int(y_cor))
            t.write(answer_state)
            # score += 1
            guessed_states.append(answer_state)
        else:
            continue

    #===================
    #Write state name




turtle.mainloop()