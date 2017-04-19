import pygame
from engine.common.object.CommonObject import CommonObject


class CircularObject(CommonObject):
    def __init__(self, center, texture, r):
        CommonObject.__init__(self, center, texture)
        self.radius = r
        self.bounding = pygame.Rect((center.x - r, center.y - r), (2*r, 2*r))

    @property
    def r(self):
        return self.radius

    @r.setter
    def r(self, value):
        self.radius = value
