from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():

    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates a car and adds it to the list"""
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-240, 250)
            new_car.goto(320, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        """Moves the cars on the screen"""
        for car in self.cars:
            car.backward(self.car_speed)

    def clear_cars(self):
        """Removes a car from the list when it surpases the x axis of the screen"""
        for car in self.cars:
            if car.xcor() < -320:
                self.cars.remove(car)
                car.reset()
                car.hideturtle()

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT