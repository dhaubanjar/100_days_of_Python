from turtle import Turtle



""" creates scoreboard class """
class Scoreboard(Turtle):               # creates scoreboard class and inherits Turtle
    def __init__(self):
        super().__init__()              # inherits everything from super class
        self.score = 0
        with open("data.txt", "r") as file:
            data = int(file.read())
        self.high_score = data
        self.penup()
        self.color("white")
        self.goto(0, 280)         # scoreboard goes to top-center of screen
        self.ht()                       # hides turtle
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} | High Score: {self.high_score} ',  align='center', font=('Arial', 16, "normal"))

    """ Increases score board upon eating food. """
    def increase_score(self):
        self.score += 1
        self.goto(0, 280)
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

