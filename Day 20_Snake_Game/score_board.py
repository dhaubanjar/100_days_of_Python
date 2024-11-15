from turtle import Turtle

""" creates scoreboard class """
class Scoreboard(Turtle):               # creates scoreboard class and inherits Turtle
    def __init__(self):
        super().__init__()              # inherits everything from super class
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 280)         # scoreboard goes to top-center of screen
        self.ht()                       # hides turtle
        self.write(f'Score: {self.score}', True, align='center', font=('Arial', 16, "normal"))


    """ Increases score board upon eating food. """
    def increase_score(self):
        self.score += 1
        self.clear()                    # clears previous result
        self.goto(0, 280)
        self.write(f'Score: {self.score}', True, align='center', font=('Arial', 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over !", True, align='center', font=('Arial', 46, "normal"))