import os
import sys
from turtle import Turtle

FONT = ("Courier", 24, "normal")

# Get the path of the main.py file and pass the path to the ScoreTracker class to create the data.txt file.
main_script_directory = os.path.dirname(os.path.realpath(__file__))
file_path = str(os.path.join(main_script_directory, "data.txt"))

# Helpers directory
helpers_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(helpers_dir)
from ProjectHelpers.ScoreTracker import ScoreTracker

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_tracker = ScoreTracker(file_path, "1")
        self.high_score = self.score_tracker.high_score
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()  # Adicione esta linha para exibir o nível inicial

    def update_scoreboard(self):
        """ Updates the scoreboard with the current score and high score. """
        self.clear()
        self.write(f"Level: {self.level} - High Score: {self.high_score}", align="left", font=FONT)

    def increase_level(self):
        """ Increases the level by 1 and updates the scoreboard with the new level when trutle crosses the road."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """ Displays the game over message and updates the high score if the current score is higher. """
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        if self.level > self.high_score:
            self.high_score = self.level
            self.score_tracker.set_high_score(self.level)
        self.level = 1
        

    
