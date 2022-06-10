import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
screen.onkeypress(player.move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()
    
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False           
            scoreboard.game_over()
    
    if player.finish():
        player.reset()
        scoreboard.got_point()
        car_manager.increase_speed()


screen.exitonclick()