from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(position)
        self.write(f'{self.score}', True, 'Center', font=('Arial', 70, 'bold'))


    def increase_score(self, position):
        self.score += 1
        self.clear()
        self.goto(position)
        self.write(f'{self.score}', True, 'Center', font=('Arial', 70, 'bold'))

    def game_over(self, position):
        self.goto(position)
        self.write(f'!! GAME OVER !!', True, 'Center', font=('Arial', 30, 'bold'))


