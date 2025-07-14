import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car_counter = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Home made Frogger")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Creating cars every 6th time
    if car_counter < 6:
        car_counter += 1
    else:
        car_manager.create_cars()
        car_counter = 0

    car_manager.move_cars()

    # Detect collision with player and car
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.reset_pos()
        scoreboard.increase_score()
        car_manager.level_up()

screen.exitonclick()
