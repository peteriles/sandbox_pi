"""Settings file for Alien Invasion"""

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen settings
        self.bg_color = (230, 230, 230)
        self.full_screen = False
        self.screen_width = 1200 # Only used if self.full_screen == False
        self.screen_height = 800 # Only used if self.full_screen == False

        # Ship settings
        self.ship_limit = 3 # Number of ships
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        self.invincible_bullets = False; 

        # Alien settings
        self.fleet_drop_speed = 30
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        
        # Speed settings
        self.alien_speed = 1.5
        self.bullet_speed = 5.0
        self.ship_speed = 3 # Horizontal speed. [1-5] 1 = slow, 5 = fast

        # Scoring settings
        self.alien_points = 50


    def increase_speed(self):
        """Increase speed settings."""
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)