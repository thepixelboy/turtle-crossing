from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.finish_line = FINISH_LINE_Y

    def move(self):
        """Moves the turtle forward on the screen"""
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Clears the turtle of the screen and moves it to the starting position"""
        self.clear()
        self.goto(STARTING_POSITION)