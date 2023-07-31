import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Status Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State's Guessed", prompt="What's another state's name?").title()
    all_state = data["state"].to_list()

    if answer_state == "Exit":
        missing_state = [ state for state in all_state if state not  in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States to learn")
        break

    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


