import turtle
import pandas as pd
screen =turtle.Screen()
screen.title("Indian States Game")
image="Indian_states.gif"
screen.addshape(image)
turtle.shape(image)
data=pd.read_csv("states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<29:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 States correct!",
                                   prompt="Whats another states name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state  not in guessed_states:
                missing_states.append(state)
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("missed_ones.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.pensize(15)
        t.hideturtle()
        t.penup()
        state_data= data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state,font=("Times New Roman",20,"bold"))



