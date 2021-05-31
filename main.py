import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setting up the screen
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

# Variables
game_is_on = True

# Creating the player
player = Player()
car_manager = CarManager()

# Listening for keypress to move the player
screen.listen()
screen.onkeypress(player.move, "Up")

# Main loop
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars and move it along the screen
    car_manager.create_car()
    car_manager.move_cars()

    # Detect the player reaching finish line (top of the screen)
    if player.ycor() > player.finish_line:
        player.reset_position()

screen.exitonclick()