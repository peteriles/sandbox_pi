"""Alien Invasion game - main file"""
import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Create screen surface object, and set game window resolution
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion!")

        # Create Ship instance
        self.ship = Ship(self)
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Event loop to watch for keyboard and mouse events
            self._check_events()

            # Update position of the ship
            self.ship.update()
            
            # Update the screen
            self._update_screen()

            # Specify frame rate (in Hz)
            self.clock.tick(60)

    def _check_events(self):
        """
        Helper method to respond to keypresses and mouse events.
        Note leading underscore "_" in name.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Stopping game.")
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False 
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """
        Helper method to update images on the screen
        and to flip to the new screen.
        """
        # Redraw the screen and ship during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
            
        # Make the most recently drawn screen visible.
        pygame.display.flip()


# Main routine
if __name__=='__main__':
    print("Starting Alien Invasion")
        
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

