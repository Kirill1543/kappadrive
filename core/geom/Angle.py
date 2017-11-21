from math import pi

from . import EPSILON


class Angle:
    def __init__(self, angle: float):
        self._radians = self._set_angle(angle)

    def __str__(self):
        return 'Angle({}r:{}d)'.format(self._radians, self._radians * 360 / (2 * pi))

    def __repr__(self):
        return self.__str__()

    def __neg__(self):
        return Angle(-self.radians)

    def __add__(self, other):
        return Angle(self._set_angle(self._radians + other.radians))

    def __sub__(self, other):
        return self.__add__(-other)

    def __eq__(self, other):
        return abs(self._radians - other.radians) < EPSILON

    def __ne__(self, other):
        return abs(self._radians - other.radians) >= EPSILON

    def __lt__(self, other):
        return self != other and self._radians < other.radians

    def __le__(self, other):
        return self == other or self._radians < other.radians

    def __gt__(self, other):
        return self != other and self._radians > other.radians

    def __ge__(self, other):
        return self == other or self._radians > other.radians

    @property
    def radians(self) -> float:
        return self._radians

    @staticmethod
    def _set_angle(angle: float) -> float:
        pi2 = 2 * pi
        while angle > pi2 - EPSILON:
            angle -= pi2

        while angle < -EPSILON:
            angle += pi2

        if abs(angle) < EPSILON:
            angle = 0.0

        return angle

    def is_between(self, left: __name__, right: __name__) -> bool:
        if self == left or self == right:
            return True
        elif left > right:
            return not self.is_between(right, left)
        else:
            return left <= self <= right
