"""Alien Invasion game - main file"""
import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Create screen surface object, and set game window resolution
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion!")

        # Create Ship instance
        self.ship = Ship(self)

        # Create group of bullets
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Event loop to watch for keyboard and mouse events
            self._check_events()

            # Update position of the ship
            self.ship.update()
            
            # Update bullet positions, manage list of active bullets
            self._update_bullets()
            
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
                print("Game window closed; stopping game.")
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Helper method to manage keydown events"""
        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            # Move ship up
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move ship down
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            print("'q' pressed; stopping game.")
            sys.exit()            

    def _check_keyup_events(self, event):
        """Helper method to manage keyup events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False 
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False            

    def _update_screen(self):
        """
        Helper method to update images on the screen
        and to flip to the new screen.
        """
        # Redraw the screen, ship, and bullets during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
            
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""

        # Update positions of bullets
        self.bullets.update()
         
        # Remove bullets that have disappear. Loop over a copy of the list of 
        # bullets since we can't modify the list we're looping over.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


# Main routine
if __name__=='__main__':
    print("Starting Alien Invasion")
        
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

