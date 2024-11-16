import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10
CAR_SIZE = (1, 2)

class CarManager:
    def __init__(self):
        self.all_cars = []              # stores the generated cars
        self.up_chance = 6

    def create_car(self):
        chance = random.randint(1, self.up_chance)          # slows the generation of cars by almost 6 main.py loop
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(CAR_SIZE[0], CAR_SIZE[1])
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)           # appends the generated cars

    def increase_speed(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
