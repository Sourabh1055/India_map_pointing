import turtle
import pandas

screen = turtle.Screen()
screen.title("India states Game")
image = "India_map.gif"
screen.addshape(image)
screen.setup(width=800,height=800)
turtle.shape(image)

data = pandas.read_csv("india_states_coordinates.csv")

all_states = data.state.tolist()
gussed_states = []

while len(gussed_states) < 34:
    answer_state = screen.textinput(f"{len(gussed_states)}/50 State's correctly.",  prompt = "What's the next state?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in gussed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Indian_States_to_learn.csv")
        break
    elif answer_state in all_states:
        gussed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
