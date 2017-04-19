import pygame
from engine.common.object.CommonObject import CommonObject
from engine.common.object.Point import Point


class RectObject(CommonObject):
    def __init__(self, corner, texture, width, height):
        CommonObject.__init__(self, Point(corner.x + width / 2.0, corner.y + height / 2.0, corner.z), texture)
        self.width = width
        self.height = height
        self.bounding = pygame.Rect((corner.x, corner.y), (width, height))

    @property
    def w(self):
        return self.width

    @w.setter
    def w(self, value):
        self.width = value

    @property
    def h(self):
        return self.height

    @h.setter
    def h(self, value):
        self.height = value

    @property
    def x(self):
        return self.center.x - self.width / 2.0

    @x.setter
    def x(self, value):
        self.center.x = value + self.width / 2.0

    @property
    def y(self):
        return self.center.y - self.height / 2.0

    @y.setter
    def y(self, value):
        self.center.y = value + self.height / 2.0
