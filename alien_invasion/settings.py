"""Settings file for Alien Invasion"""

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.bg_color = (230, 230, 230)
        self.full_screen = False
        self.screen_width = 1200 # Only used if self.full_screen == False
        self.screen_height = 800 # Only used if self.full_screen == False

        # Ship settings
        self.speed = 3 # Horizontal speed. [1-5] 1 = slow, 5 = fast

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100
