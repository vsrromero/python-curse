from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(0,0,0)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.snake_head.distance(food) < 10:
        food.spawn_food()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.snake_head.xcor() > 295 or snake.snake_head.xcor() < -295 or snake.snake_head.ycor() > 295 or snake.snake_head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
