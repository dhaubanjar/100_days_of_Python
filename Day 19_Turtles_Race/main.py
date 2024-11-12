import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)                         # sets screen height and width
""" Takes input from the user """
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the bet? Enter a color: ")
colors = ["red", "orange", "brown", "green", "blue", "violet"]
y_positions = [-160, -105, -35, 35, 105, 160]               # variable y-coordinates for multiple turtle's position
all_turtles = []                                            # adds multiple turtles in a list


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")                         # instantiates Turtle class and passing shape attribute
    new_turtle.color(colors[turtle_index])                      # selects 0 index color from colors list
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])            # sets starting point for all turtles
    all_turtles.append(new_turtle)                                  # stores all generated turtles in a list
try:
    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 200:                                 # checks if any turtle reached an end
                is_race_on = False                                  # flag set to false
                winner = turtle.fillcolor()                         # store the winner's color in the winner variable
                if winner == user_bet:
                    print(f"You've won! The {winner} turtle is the winner!")
                else:
                    print(f"You've lost! The {winner} turtle is the winner!")

            random_distance = random.randint(0,15)              # randomize forward() for every turtles.
            turtle.forward(random_distance)
except NameError:
    print("Please enter a valid turtle color!")


screen.exitonclick()