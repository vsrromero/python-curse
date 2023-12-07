from turtle import Turtle

PADDLE_MOVEMENT: int = 30
PADDLE_COLOR: tuple = (1,1,1)
PADDLE_LEN: int = 1
PADDLE_WID: int = 5
PADDLE_SHAPE: str = 'square'

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape(PADDLE_SHAPE)
        self.speed(0)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_len=PADDLE_LEN, stretch_wid=PADDLE_WID)
        self.goto(position)
        
    def move_paddle_up(self):
        new_y = self.ycor() + PADDLE_MOVEMENT
        self.goto(self.xcor(), new_y)

    def move_paddle_down(self):
        new_y = self.ycor() - PADDLE_MOVEMENT
        self.goto(self.xcor(), new_y)
