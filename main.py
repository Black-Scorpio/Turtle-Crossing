import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()


# Listen for up key sound
screen.listen()
screen.onkeypress(player.go_up, 'w')
screen.onkeypress(player.go_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(0.07)
    screen.update()
    cars.create_car()
    cars.car_movement()
    # Detect Collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if player reached the other side
    if player.ycor() > 290:
        cars.level_up()
        scoreboard.level_increase()
        player.reset_position()


screen.exitonclick()
