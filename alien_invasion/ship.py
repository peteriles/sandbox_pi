"""Module containing the Ship class"""

import sys
import pygame

from settings import Settings

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = Settings()

        # Create surface representing the ship. 
        # Also, load the ship image and get its rect.
        try:
            self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        except FileNotFoundError:
            print("No image file found at specified location.")
            print("Stopping game.")
            sys.exit()
        else:
            self.rect = self.image.get_rect()

            # Start each new ship at the bottom centre of the screen.
            self.rect.midbottom = self.screen_rect.midbottom

            # Movement flags; start with a ship that's not moving
            self.moving_right = False
            self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += self.settings.speed
        if self.moving_left:
            self.rect.x -= self.settings.speed

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)