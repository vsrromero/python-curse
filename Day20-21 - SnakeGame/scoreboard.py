import os
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color(1,1,1)
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """ Updates the scoreboard with the current score and high score. """
        self.write(f"Score: {self.score} - High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
       

    def game_over(self):
        """ Displays the game over message and updates the high score if the current score is higher. """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()

    def increase_score(self):
        """ Increases the score by 1 and updates the scoreboard with the new score when the snake eats the food. """
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def get_high_score(self):
        """ Gets the high score from the data.txt file. """
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data.txt")
        try:
            with open(file_path, mode="r") as data:
                self.high_score = int(data.read())
                return self.high_score
        except FileNotFoundError:
            return 0
    
    def set_high_score(self):
        """ Sets the high score in the data.txt file. """
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data.txt")
        with open(file_path, mode="w") as data:
            data.write(str(self.score))
