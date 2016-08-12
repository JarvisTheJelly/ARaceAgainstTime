"""This file contains the class for the background"""

import pygame
import random
import Entity
import gametools


class Background(object):
    """The background contains all the entities that do
    not collide with anything but are there for scenery
    (stars, planets, stations, etc)."""

    def __init__(self, screen_size, entity_goal=250):
        """Set up basic variables, as well as call the function
        to populate the background"""

        self.entity_list = []

        # The number of entities the screen should roughly have
        self.entity_goal = entity_goal

        self.screen_size = screen_size
        self.populate(self.screen_size, True)

    def populate(self, screen_size, first=False):
        num_entities = self.entity_goal - len(self.entity_list)
        for i in xrange(num_entities):
            if first:
                random_pos = gametools.vector2.Vector2(random.randint(0, screen_size[0]), 
                                                       random.randint(0, screen_size[1]))

            else:
                random_pos = gametools.vector2.Vector2(screen_size[0], random.randint(0, screen_size[1]))

            width = random.uniform(2, 7)
            distance = (1.0 / (2 ** width)) * (2 ** 7)
            random_img = pygame.Surface((int(width), int(width)))

            random_img.fill((255, 255, 255))

            entity_to_add = Entity.Entity(random_pos, random_img, distance)

            self.entity_list.append(entity_to_add)

    def update(self, speed):
        """Updates all the entities and checks to see if they
        go off the screen. If so, REMOVE THEM.
        
        speed is how fast the screen is scrolling.
        """

        garbage_collection = []
        for entity in self.entity_list:
            entity.update(speed)
            if entity.pos.x < 0:
                garbage_collection.append(entity)

        for entity in garbage_collection:
            self.entity_list.remove(entity)

        self.populate(self.screen_size)

    def render(self, surface):
        """Render all the entities to the given surface"""

        for entity in self.entity_list:
            entity.render(surface)
