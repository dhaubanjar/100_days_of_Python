import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

entered_states = []

while len(entered_states) < 50:
    answer_state = screen.textinput(title=f"{len(entered_states)}/50 States Correct", prompt="What's another state's name?").title()

    """ Reads csv file using pandas """
    data = pd.read_csv("50_states.csv")
    all_states = data.state.to_list()           # converts series to list to be able to iterate

    if answer_state == "Exit":                  # Terminates the program
        missing_states = []
        for state in all_states:                # checks for the missing states
            if state not in entered_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)     # creates dataframe of missing states
        new_data.to_csv("missing_states.csv")       # exports the csv file
        break

    if answer_state not in entered_states:      # checks if it is already guessed
        if answer_state in all_states:
            t =turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(state_data["x"].item(), state_data["y"].item())
            t.write(state_data["state"].item(), align="center", font=("Roboto", 14, "bold"))    # writes on screen
            entered_states.append(answer_state)             # appends correct answers
    else:
        pass

screen.exitonclick()
screen.mainloop()
