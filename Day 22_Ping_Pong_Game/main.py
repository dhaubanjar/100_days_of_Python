from turtle import Screen
from paddle import Paddle
from pong import Pong
import time

from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)                        # turns off the animation, so have to refresh it manually

r_paddle = Paddle((370, 0))             # creates r_paddle object from class Paddle and passes value
l_paddle = Paddle((-380, 0))            # creates l_paddle object from class Paddle and passes value
pong = Pong()
r_scoreboard = Scoreboard((200,200))
l_scoreboard = Scoreboard((-200, 200))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
count = 0
while game_is_on:
    time.sleep(pong.add_speed)                                  # adds speed of the pong once it hit the paddle
    screen.update()
    pong.move()

    if pong.ycor() > 270 or pong.ycor() < -270:                 # limits y-axis to 270 and bounce
        pong.bounce()

    elif pong.xcor() > 356 and pong.distance(r_paddle) < 50:    # sets bounce when encounters right paddle
        pong.paddle_bounce()

    elif pong.xcor() < -356 and pong.distance(l_paddle) < 50:   # sets bounce when encounters left paddle
        pong.paddle_bounce()

    elif pong.xcor() > 400:                                     # increases left score when right paddle misses
        l_scoreboard.increase_score((-200, 200))
        pong.reset_position()
        count += 1
        if count == 3:
            game_is_on = False
            r_scoreboard.game_over((0,0))

    elif pong.xcor() < -400:                                    # increases right score when left paddle misses
        r_scoreboard.increase_score((200, 200))
        pong.reset_position()
        count += 1
        if count == 3:
            game_is_on = False
            r_scoreboard.game_over((0, 0))
















screen.exitonclick()