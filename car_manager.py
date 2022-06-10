from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        chance_show_car = random.randint(1, 5)
        if chance_show_car == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.goto(x=320, y=random.randint(-250, 250))
            self.cars.append(car)
    
    def move(self):
        for move_car in range(len(self.cars) - 1):
            self.cars[move_car].backward(self.car_speed)
    
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        
        
    
        

    
    
  