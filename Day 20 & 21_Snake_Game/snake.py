from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()             # auto calls create_snake() method
        self.head = self.snake_body[0]  # snake_body[0] is used many times so why not define here

    """ Creates a snake """
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    """ adds snake  """
    def add_snake(self, position):
        snake_segment = Turtle(shape='square')
        snake_segment.color('white')
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake_body.append(snake_segment)

    """ adds snake to snake body after encountering the food """
    def extend_snake(self):
        self.add_snake(self.snake_body[-1].position())

    """ moves whole snake forward """
    def move_snake(self):
        for body in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x, new_y)  # last body goes to 2nd last position, 2nd last to previous
        self.head.forward(MOVE_DISTANCE)

    def snake_reset(self):
        for segment in self.snake_body:
            segment.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

