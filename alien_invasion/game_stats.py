"""Module that contains GameStats class"""
from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Load high score from file if file exists. Set to 0 otherwise.
        # Initializing high score in __init__ since high score should never be 
        # reset.
        self.high_score_file_path = Path("alien_invasion/highscore.txt")
        try: 
            self.high_score = int(self.high_score_file_path.read_text())
        except:        
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.level = 1
        self.score = 0