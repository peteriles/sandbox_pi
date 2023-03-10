"""Bullet classes"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game, invincible_bullet=False):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        if invincible_bullet:
            self.color = self.settings.invincible_bullet_color    
        else:
            self.color = self.settings.bullet_color

    def update(self):
        """Move the bullet"""

        # Update the exact position of the bullet
        self.y += self.velocity_y
        self.x += self.velocity_x

        # Update the rect position
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class ShipBullet(Bullet):
    """Represents a specific type of bullet - one coming from the ship"""

    def __init__(self, ai_game, invincible_bullet):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to a ship's bullet
        """
        super().__init__(ai_game, invincible_bullet)

        # Create a bullet rect at (0, 0) and the set the correct position 
        # relative to the ship
        self.rect = pygame.Rect(0, 0, 
            self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Bullets should move horizontally according to how the ship is moving
        if ai_game.ship.moving_right == True:
            self.velocity_x = ai_game.settings.ship_speed
        elif ai_game.ship.moving_left == True:
            self.velocity_x = -ai_game.settings.ship_speed
        else:
            self.velocity_x = 0

        if ai_game.ship.moving_up == True:
            self.velocity_y = -ai_game.settings.ship_speed - self.settings.bullet_speed
        elif ai_game.ship.moving_down == True:
            self.velocity_y = ai_game.settings.ship_speed - self.settings.bullet_speed
        else:
            self.velocity_y = -self.settings.bullet_speed
    
        # Store the bullet's position as a float
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)


class AlienBullet(Bullet):
    """Represents a specific type of bullet - one coming from an alien"""

    def __init__(self, ai_game, alien_instance):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to a ship's bullet
        """
        super().__init__(ai_game)

        # Create a bullet rect at (0, 0) and the set the correct position 
        # relative to the alien
        self.rect = pygame.Rect(0, 0, 
            self.settings.alien_bullet_width, self.settings.alien_bullet_height)
        self.rect.midbottom = alien_instance.rect.midbottom
        
        # Alien bullets just go straight down, for now
        self.velocity_x = 0
        self.velocity_y = self.settings.alien_bullet_speed
    
        # Store the bullet's position as a float
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)