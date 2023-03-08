"""Module to contain RandomWalk class"""
from random import choice
from random import randint

class RandomWalk:
    """RandomWalk class"""
    def __init__(self, num_steps=10_000):

        self.num_steps = num_steps

        self.walk_x, self.walk_y = self._create_walk()

    def _create_walk(self):
        """Create a random walk"""
        walk_x = [0]
        walk_y = [0]

        # Build walk
        for i in range(self.num_steps):
            # Get a random direction (we can move in x, y, or both directions at once)
            current_direction_x = choice([-1, 0, 1])
            current_direction_y = choice([-1, 0, 1])

            # Get a random distance (this is applied to both the x and y directions)
            current_distance = randint(1, 5)

            walk_x.append(walk_x[-1] + current_direction_x*current_distance)
            walk_y.append(walk_y[-1] + current_direction_y*current_distance)

        return walk_x, walk_y