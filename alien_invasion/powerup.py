"""Module containing the Powerup class"""

import sys
import pygame
from pygame.sprite import Sprite

class Powerup(Sprite):
    """A class to manage the powerup objects."""

    def __init__(self, ai_game, powerup_type):
        """Initialize the powerup image"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.powerup_type = powerup_type

        if self.powerup_type == 'bullet_width':
            self._create_image('alien_invasion/images/bullet_width.bmp')
        elif self.powerup_type == 'num_bullets':
            self._create_image('alien_invasion/images/num_bullets.bmp')
        elif self.powerup_type == 'invincible_bullets':
            self._create_image('alien_invasion/images/invincible_bullets.bmp')
        elif self.powerup_type == 'bullet_speed':
            self._create_image('alien_invasion/images/bullet_speed.bmp')


    #invincible_bullets', 'bullet_speed            
            
    def _create_image(self, image_path):
        """Load powerup image file and create powerup image"""
        try:
            self.image = pygame.image.load(image_path)
        except FileNotFoundError:
            print("No powerup image file found at specified location.")
            print("Stopping game.")
            sys.exit()

        self.rect = self.image.get_rect()





    
        
