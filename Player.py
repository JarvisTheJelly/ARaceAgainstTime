"""The player class. This will extend the Entity class
for collision, but will add stuff like movement and health.
Similar to Enemy class."""

import pygame
import Entity


class Player(Entity.Entity):
    """The Player class (explained above)"""

    def __init__(self, pos):
        """The initialization of the player class."""

        # player_img = pygame.image.load("res/Player.png").convert()
        player_img = pygame.Surface((64, 64))
        player_img.fill((255, 255, 255))

        Entity.Entity.__init__(self, pos, player_img)
