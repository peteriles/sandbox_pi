"""Module containing the Alien class"""

import sys
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage the aliens."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        try:
            self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        except FileNotFoundError:
            print("No image file found at specified location.")
            print("Stopping game.")
            sys.exit()

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen 
        # (adjust for the size of the alien)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact (float) position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien to the right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)