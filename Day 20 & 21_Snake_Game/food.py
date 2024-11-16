from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("green")
        self.speed("fastest")
        random_x = random.randint(-270, 270)        # gives random number between -270 and 270
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

    def change_location(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)