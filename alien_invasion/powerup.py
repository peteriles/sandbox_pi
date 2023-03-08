"""Module containing the Powerup class"""

import sys
import pygame
from pygame.sprite import Sprite

class Powerup(Sprite):
    """A class to manage the powerup objects."""

    def __init__(self, ai_game):
        """Initialize the powerup and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the powerup image and set its rect attribute.
        try:
            self.image = pygame.image.load('alien_invasion/images/pow.bmp')
        except FileNotFoundError:
            print("No powerup image file found at specified location.")
            print("Stopping game.")
            sys.exit()

        self.rect = self.image.get_rect()

        # Start each new powerup in a random spot on the screen
        self.rect.x = 300
        self.rect.y = 300
