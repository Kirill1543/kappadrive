from math import pi

from kappa.core.geom import EPSILON


class Angle:
    @staticmethod
    def set_angle(angle: float):
        pi2 = 2 * pi
        while angle > pi2:
            angle -= pi2

        while angle < 0:
            angle += pi2

        return angle

    def __init__(self, angle: float):
        self._angle = self.set_angle(angle)

    def __str__(self):
        return 'Angle({}r:{}d)'.format(self._angle, self._angle * 360 / (2 * pi))

    def __repr__(self):
        return self.__str__()

    @property
    def angle(self):
        return self._angle

    def __neg__(self):
        return Angle(-self.angle)

    def __add__(self, other):
        return Angle(self.set_angle(self._angle + other.angle))

    def __sub__(self, other):
        return self.__add__(-other)

    def __eq__(self, other):
        return abs(self._angle - other.angle) < EPSILON
