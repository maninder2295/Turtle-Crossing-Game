from turtle import  Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_scoreboard()

    def create_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.color("black")
        self.write(f"Level {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.create_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align='center', font=FONT)

