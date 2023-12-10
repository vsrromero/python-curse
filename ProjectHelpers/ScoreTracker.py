import os

class ScoreTracker:
    
    def __init__(self, file_path, initial_score) -> None:
        self.file_path = file_path
        self.create_data_file(initial_score)
        self.high_score = self.get_high_score()
        print(f"File path: {self.file_path}")
        
    def create_data_file(self, initial_score):
        """ Creates the data.txt file if it does not exist. """
        try:
            if not os.path.exists(self.file_path):
                with open(self.file_path, mode="w") as data:
                    data.write(initial_score)
        except Exception as e:
            print(f"Error creating data file: {e}")
                
    def get_high_score(self):
        """ Gets the high score from the data.txt file. """
        try:
            with open(self.file_path, mode="r") as data:
                self.high_score = int(data.read())
                return self.high_score
        except FileNotFoundError:
            return 0
        except Exception as e:
            print(f"Error getting high score: {e}")
    
    def set_high_score(self, score):
        """ Sets the high score in the data.txt file. """
        try:
            with open(self.file_path, mode="w") as data:
                data.write(str(score))
        except Exception as e:
            print(f"Error setting high score: {e}")
