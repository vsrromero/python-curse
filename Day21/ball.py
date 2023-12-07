from turtle import Turtle
import random
from game_screen import GameScreen

game_screen = GameScreen()

BALL_SIZE: dict[str, float] = {'length': 1, 'width': 1}
BALL_START_POSITION: tuple[float, float] = (0,0)
BALL_FORMAT: str = 'circle'
BALL_COLOR: tuple = (1,1,1)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=BALL_SIZE['length'], stretch_wid=BALL_SIZE['width'])
        self.goto(BALL_START_POSITION)
        self.shape(BALL_FORMAT)
        self.color(BALL_COLOR)
        
    def ball_start(self):
        x_axis_move = random.randint(0,1) # choose wich side the ball will start moving, left or right
        
        if x_axis_move > 0:
            self.goto(game_screen.screen_width / 2, random((game_screen.screen_height / 2) * -1, game_screen.screen_height / 2))