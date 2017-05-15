from math import hypot


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def level(self):
        return self.z

    @level.setter
    def level(self, value):
        self.z = value

    @property
    def coords(self):
        return [self.x, self.y, self.z]

    @coords.setter
    def coords(self, value):
        self.x, self.y, self.z = value

    def distance_to(self, x, y):
        return hypot(x - self.x, y - self.y)

    def distance_to_point(self, p):
        return self.distance_to(p.x, p.y)
