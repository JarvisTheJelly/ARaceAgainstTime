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

        self.planets = [pygame.image.load('res/Planets/Planet1.png').convert(),
                        pygame.image.load('res/Planets/Planet2.png').convert(),
                        pygame.image.load('res/Planets/Planet3.png').convert()]

        for planet in self.planets:
            planet.set_colorkey((255, 0, 255))

        self.populate(self.screen_size, True)

    def populate(self, screen_size, first=False):
        """Add all the entities to the background. Entities spawn from
        the right side of the screen."""

        num_entities = self.entity_goal - len(self.entity_list)
        for i in xrange(num_entities):
            if first:
                random_pos = gametools.vector2.Vector2(random.randint(0, screen_size[0]), 
                                                       random.randint(0, screen_size[1]))

            else:
                random_pos = gametools.vector2.Vector2(screen_size[0], random.randint(0, screen_size[1]))

            if random.randint(0, 999) == 0 or (first and random.randint(0, 9) == 0):
                # Add a star
                width = random.uniform(3, 7)
                random_img = pygame.Surface((int(width), int(width)))
                random_img.fill((255, 255, 255))
                distance = 75

            elif random.randint(0, 499) == 0:
                # Add a planet
                width = random.uniform(2, 7)
                random_img = random.choice(self.planets)
                scale = (width-2) / 5
                random_img = pygame.transform.scale(random_img, (int(random_img.get_width() * scale),
                                                                 int(random_img.get_height() * scale)))
                random_pos.x += random_img.get_width()
                distance = (1.0 / (2 ** width)) * (2 ** 7)

            else:
                # Add a dust particle
                width = random.uniform(2, 7)
                random_img = pygame.Surface((int(width), int(width)))
                random_img.fill((139, 121, 94))
                distance = (1.0 / (2 ** width)) * (2 ** 3)

            entity_to_add = Entity.Entity(random_pos, random_img, distance)

            self.entity_list.append(entity_to_add)

    def update(self, speed):
        """Updates all the entities and checks to see if they
        go off the screen. If so, REMOVE THEM.
        
        speed is how fast the screen is scrolling.
        """

        self.entity_list = sorted(self.entity_list, key=lambda Entity: -Entity.distance)

        garbage_collection = []
        for entity in self.entity_list:
            entity.update(speed)
            if entity.pos.x + (0.5 * entity.img.get_width()) < 0:
                garbage_collection.append(entity)

        for entity in garbage_collection:
            self.entity_list.remove(entity)
            del entity

        self.populate(self.screen_size)

    def render(self, surface):
        """Render all the entities to the given surface"""

        for entity in self.entity_list:
            entity.render(surface)
