from turtle import Turtle

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BGCOLOR = (0,0,0)

class GameScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.bg_color = BGCOLOR


        

        