import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road Crossing")
screen.bgcolor('black')
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    """ Access create_car object from car_manager class """
    car.create_car()
    car.increase_speed()

    """ Detect collision with car """
    for c in car.all_cars:
        if c.distance(player) < 25:     # detects collision
            game_is_on = False
            score.game_over()


    """ Detects crossing and changes level """
    if player.ycor() > 280:
        car.up_chance -= 1              # decreases value of chance variable to generate number of cars.
        score.increase_level()          # increases level
        player.reposition()             # sets position of player to the beginning






screen.exitonclick()