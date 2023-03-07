"""
Alien Invasion game - main file

Ideas for improvements:
- power-ups that you need to drive over to activate:
    - stronger bullets (e.g. that pass through aliens)
- ability to turn ship
- practice mode
- two-player game
- maybe game doesn't end when aliens hit the bottom?
- save high scores and names in a file
"""
import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        # Create an instance to store game statistics, and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Create Ship instance
        self.ship = Ship(self)

        # Create group of bullets
        self.bullets = pygame.sprite.Group()

        # Create the aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Start game in an inactive state.
        self.game_active = False

        # Make the Play button
        self.play_button = Button(self, "Play")
        
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Event loop to watch for keyboard and mouse events
            self._check_events()

            if self.game_active:

                # Update position of the ship
                self.ship.update()
            
                # Update bullet positions, manage list of active bullets
                self._update_bullets()
            
                # Update the aliens
                self._update_aliens()
            
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
            
            # Reset the game statistics.
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            
            self.game_active = True
    
            # Get rid of any remaining bullets and aliens                        
            self.bullets.empty()
            self.aliens.empty()

            # Create a new alien fleet and centre the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    
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
        # Redraw the screen, ship, bullets, and aliens during each pass through
        # the loop.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the stats to the screen.
        self.sb.show_stats()

        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()
            
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens."""

        # Create an alien and keep adding them until there's no room left.
        # Spacing between aliens is one alien width and one height.
        alien = Alien(self)
        
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 *alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2*alien_width

            # Finished a row; reset x value, and increment y value
            current_x = alien_width
            current_y += 2*alien_height

        self.aliens.add(alien)
    
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        
        # Change fleet direction
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """
        Update position of bullets, get rid of old bullets, and check for bullet-
        alien collisions.
        """

        # Update positions of bullets
        self.bullets.update()

        # Remove bullets that have disappeared. Loop over a copy of the list of 
        # bullets since we can't modify the list we're looping over.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()        

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions. 
        # This function's arguments are a sprit (ship) and a group (aliens)
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""

        # Remove any bullets and aliens that have collided
        # Check for any bullets that have hit aliens. If so, get rid of the bullet
        # and the alien. 
        # The 'groupcollide' function returns a dictionary of collisions 
        # (bullet : alien). "True" arguments indicate that both parties to the 
        # collision are to be deleted.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, 
                                                not self.settings.invincible_bullets, 
                                                True)
        
        if collisions:
            for aliens in collisions.values():
                # Loop over each value in the collisions dictionary. Each value
                # is a list of aliens hit by a single bullet
                self.stats.score += len(aliens) * self.settings.alien_points
            
            self.sb.prep_score()
            self.sb.check_high_score()

        # Check if we've destroyed all the aliens
        if not self.aliens:
            # Increment level
            print(f'Level {self.stats.level} complete! New aliens approach..')
            self.stats.level += 1
            self.sb.prep_level()
            
            # Destroy existing bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()


    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            print("Ship hit!!!")
            print("    Number of ships remaining = : ", self.stats.ships_left)

            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create a new alien fleet and centre the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)

        else:
            # We have run out of ships
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

# Main routine
if __name__=='__main__':
    print("Starting Alien Invasion")
        
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()