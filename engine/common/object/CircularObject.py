import pygame


# Interface
class CircularObject:
    def __init__(self, r):
        self.radius = r

    @property
    def r(self):
        return self.radius

    @r.setter
    def r(self, value):
        self.radius = value

    @property
    def bounding(self):
        return pygame.Rect((self.center.x - self.radius, self.center.y - self.radius), (2*self.radius, 2*self.radius))
