import os, sys
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

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
        self.score = 0
        self.score_tracker = ScoreTracker(file_path, "0")
        self.high_score = self.score_tracker.high_score
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
            self.score_tracker.set_high_score(self.score)

    def increase_score(self):
        """ Increases the score by 1 and updates the scoreboard with the new score when the snake eats the food. """
        self.score += 1
        self.clear()
        self.update_scoreboard()
        