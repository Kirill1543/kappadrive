import pygame


# Interface
class RectObject:
    def __init__(self, width, height):
        self.width = width
        self.height = height

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

    @property
    def bounding(self):
        return pygame.Rect((self.x, self.y), (self.width, self.height))
