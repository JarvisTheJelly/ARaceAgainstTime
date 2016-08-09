"""This file will contain just the base class for Entity,
the most basic class"""


class Entity(object):
    """This class will handle most things, from
    racers to obstacles to markers. """

    def __init__(self, pos, img):
        """Initializes the Entity.
        
        Args:
            pos - The position of the Entity (in it's center)
            img - The image used to draw the Entity."""
        
        self.collision = False
        self.pos = pos
        self.img = img
        self.rect = img.get_rect()
        self.rect.center = pos

    def test_collision(self, other_entity):
        """Tests to see if this entity is colliding
        with another entity. """

        if self.rect.colliderect(other_entity.rect) and self.collision:
            return True

        return False

    def update(self):
        """The update function called for the Entity. This
        updates the position and rect of the Entity."""

        self.rect.center = self.pos

    def render(self, surface):
        """Renders the Entity onto the given surface using
        the Entity's own rect."""

        surface.blit(self.img, self.rect)
