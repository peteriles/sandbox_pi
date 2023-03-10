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
        self.bullet_color = (60, 60, 60)
        self.invincible_bullet_color = (255, 165, 0)
        self.bullets_allowed_increment = 2
        self.bullet_width_increase = 5
        self.bullet_height_increase = 5
        self.bullet_speed_increase = 2

        # Alien settings
        self.fleet_drop_speed = 30
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        # Number of free rows at the bottom of the screen at game start
        self.free_alien_rows = 6 
        # Number of columns at the side of the screen at game start
        self.free_alien_columns = 3

        # Alien Bullet settings
        self.alien_bullet_width = 7 # Increases with powerups   
        self.alien_bullet_height = 7
        self.alien_bullet_speed = 5
        

        # Powerup settings
        self.powerup_period = 300 # Roughly how many frames to wait for the 
                                  # next powerup appearance/disappearance
        self.powerup_options = ['bullet_width', 
                                'num_bullets', 
                                'invincible_bullets', 
                                'bullet_speed']
        self.powerup_buffer_pixels = 50; # Powerups will appear at least this 
                                         # far from screen edges

        # How quickly the game speeds up with each level
        self.speedup_scale = 1.1

        # How quickly the alien point values increase with each level
        self.score_scale = 1.5

        # How quickly alien-bullet speeds increase
        self.alien_bullet_speed_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        
        # Speed settings
        self.alien_speed = 1.5
        self.bullet_speed = 5.0 # Also changes with powerup
        self.ship_speed = 3 # Horizontal speed. [1-5] 1 = slow, 5 = fast

        # Bullet settings
        self.bullets_allowed = 3 # Increases with powerups
        self.bullet_width = 3 # Increases with powerups   
        self.bullet_height = 15 # Increases when speed increses
                                # (to deal with frame rate issues)
        self.invincible_bullets = False; # Changes with powerup

        # Alien bullet settings
        self.alien_fire_period = 150

        # Scoring settings
        self.alien_points = 50


    def increase_speed(self):
        """Increase speed settings."""
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_height *= self.speedup_scale
        self.alien_fire_period = round(self.alien_fire_period/self.alien_bullet_speed_scale)

        self.alien_points = int(self.alien_points * self.score_scale)