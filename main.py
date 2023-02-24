import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()

answer_state = screen.textinput(title="Guess State", prompt="What is another state?")

data = pd.read_csv("50_states.csv")
state_name_list = data.state.tolist()

for x in state_name_list:
    if answer_state.lower() == x.lower():
        print("in list")
    else:
        continue

x_cor = (data[(data.state) == answer_state]).loc[:,"x"]
y_cor = (data[(data.state) == answer_state]).loc[:,"y"]

print(type(int(x_cor)))
print(y_cor)

#===================
#Write state name
t.penup()
t.goto(int(x_cor), int(y_cor))
t.write(answer_state)


turtle.mainloop()