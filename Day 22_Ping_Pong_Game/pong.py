from turtle import Turtle

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.add_speed = 0.1

    """ starts moving the ball """
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    """ Detect collision with top and bottom walls """
    def bounce(self):
        self.y_move *= -1

    """ Detect collision with both paddles """
    def paddle_bounce(self):
        self.x_move *= -1
        self.add_speed *= 0.9

    """ Detect the missed balls """
    def reset_position(self):
        self.goto(0, 0)
        self.add_speed = 0.1
        self.paddle_bounce()
