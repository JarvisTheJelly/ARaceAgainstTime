"""This file contains the class for the background"""

import Entity
import random
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

        self.populate_stars(screen_size)

    def populate(self, screen_size):
        num_entities = self.entity_goal - len(self.entity_list)
        for i in xrange(num_entities):
            random_pos = gametools.vector2.Vector2(0,
                                                   random.randint(0, screen_size[1]))
            random_img = pygame.Surface((random.randint(2, 4),
                                         random.randint(2, 4)))
            random_img.fill((255, 255, 255))

            entity_to_add = Entity.Entity(random_pos, random_img)

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

    def render(self, surface):
        """Render all the entities to the given surface"""

        for entity in self.entity_list:
            entity.render(surface)
