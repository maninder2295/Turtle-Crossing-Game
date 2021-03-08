from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.turtlesize(stretch_wid=0.8,stretch_len=0.9)
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.up()

    def up(self):
        self.setheading(90)
        self.forward(10)

    def start_again(self):
        self.goto(STARTING_POSITION)

