from turtle import Screen
import time

from score_board import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)     # sets screen size
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)                    # refreshes the screen

""" importing custom CLASSES """
snake = Snake()                     # creates an object of the class
# snake.create_snake()              # calls create_snake() but defined inside constructor so does not need to call
food = Food()                       # initializes Food class
scoreboard = Scoreboard()           # initializes Scoreboard class

screen.listen()                     # listens to the keyboard keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()                 # helps with the animation
    time.sleep(0.1)                 # delays the animation by 0.5 sed
    snake.move_snake()


    """ Detect collisions between snake and food """
    if snake.head.distance(food) < 15:
        snake.extend_snake()                # adds new segment
        food.change_location()              # randomizes food's location
        scoreboard.increase_score()         # calls increase_score method of score_board.py

    """ Detect collisions between snake and wall """
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.reset()              # reset the score and update high score
        snake.snake_reset()

    """ Detect collisions with snake body """
    for body in snake.snake_body[1:]:               # uses python slice, [1: ] excludes 1st element
        if snake.head.distance(body) < 10:          # touches snake's body
            scoreboard.reset()
            snake.snake_reset()









screen.exitonclick()