import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_cars()
    carmanager.move_cars()

    # detection of car hit
    for car in carmanager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

    #reached finish line
    if player.is_at_finish_line():
        carmanager.level_up()
        scoreboard.increase_score()
        player.go_to_start()


screen.exitonclick()
