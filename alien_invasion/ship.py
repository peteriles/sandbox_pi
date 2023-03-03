"""Module containing the Ship class"""

import sys
import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        # Create surface representing the ship. 
        # Also, load the ship image and get its rect.
        try:
            self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        except FileNotFoundError:
            print("No image file found at specified location.")
            print("Stopping game.")
            sys.exit()
        
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom centre of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store floats for the ship's exact position
        # Initialize these values to the the existing self.rect.x/y values.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags; start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update the rect object from self.x/y (this will round the values)
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Place the ship at the bottom center of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)