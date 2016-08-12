"""This file will contain the class for the game handler.
This class will handle all of the entities, collision,
scripting, etc. """

import pygame
import Background

class GameHandler(object):
    """The game_handler class. As said above, this will
    handle all of the things that change in the game."""

    def __init__(self, screen_size):
        """Very simply initializes the class"""

        # The game states are different forms the game could be in.
        # If you are in a menu, the state would be MENU, and if you
        # are playing the game, you would be in GAME. More will be
        # added as needed
        self.game_states = ["MENU",
                            "GAME"]

        self.current_state = "MENU"

        #TODO: For background, make a class that generates a
        #star field with planets that update (thing of the space
        #school demo project
        self.background = pygame.Surface(screen_size)
        
        self.entities = []

    def menu_background(self):


    def update_entities(self):
        for entity in self.entities:
            entity.update()

    def update(self):
        self.update_entities()

    def render(self, surface):
        self.background.fill((0, 0, 0))

        surface.blit(self.background, (0, 0))

        for entity in self.entities:
            entity.render(surface)
