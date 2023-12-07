from turtle import Screen
from paddle import Paddle
from game_screen import GameScreen
from ball import Ball

game_screen = GameScreen()
width = game_screen.screen_width
height = game_screen.screen_height
bgcolor = game_screen.bg_color

screen = Screen()
screen.setup(width=width, height=height)
screen.bgcolor(bgcolor)
screen.title('Pong')

screen.tracer(0)


l_paddle_starting_position = (((width / 2) * 0.9) * -1 ,0) # (10% of the screen length away from the left screen edge, 0)
r_paddle_starting_position = (((width / 2) * 0.9), 0) # (10% of the screen length away from the right screen edge, 0)

left_paddle = Paddle(l_paddle_starting_position)
right_paddle = Paddle(r_paddle_starting_position)
screen.onkeypress(left_paddle.move_paddle_up, 'w')
screen.onkeypress(left_paddle.move_paddle_down, 's')
screen.onkeypress(right_paddle.move_paddle_up, 'Up')
screen.onkeypress(right_paddle.move_paddle_down, 'Down')

ball = Ball()

game_is_on = True

while game_is_on:
    screen.update()
    screen.listen()

screen.exitonclick()