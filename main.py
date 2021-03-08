import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
screen.listen()
screen.onkey(player.up, "Up")

# Scoreboard
scoreboard = Scoreboard()
scoreboard.create_scoreboard()
x = 0.1
game_is_on = True
while game_is_on:
    time.sleep(x)
    car_manager.generate_cars()
    car_manager.move()
    screen.update()

    # create cars with using while loop

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with finish line
    if player.ycor() > 290:
        scoreboard.increase_level()
        player.start_again()
        x *= 0.75



screen.exitonclick()
