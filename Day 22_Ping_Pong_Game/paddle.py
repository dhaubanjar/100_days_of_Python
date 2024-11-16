from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)            # sets the height and width of the paddle
        self.penup()
        self.goto(position)             # sets the provided position from main.py


    def up(self):
        new_y = self.ycor() + 50            # moves forward by adding 50 pixels
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 50            # moves opposite side by adding 50 pixels
        self.goto(self.xcor(), new_y)