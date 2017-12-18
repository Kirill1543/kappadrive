from math import acos

from . import EPSILON, Coordinates


class Vector(Coordinates):
    def __init__(self, *args):
        super().__init__(*args)

    def __neg__(self):
        return Vector(*list(-x for x in self.coords))

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("Not supported to add non-Vector to Vector")
        return Vector(*list(x + y for x, y in zip(self.coords, other.coords)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("Not supported to sub non-Vector from Vector")
        return Vector(*list(x - y for x, y in zip(self.coords, other.coords)))

    def __iadd__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("Not supported to iadd non-Vector to Vector")
        self.coords = list(x + y for x, y in zip(self.coords, other.coords))
        return self

    def __isub__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("Not supported to isub non-Vector from Vector")
        self.coords = list(x - y for x, y in zip(self.coords, other.coords))
        return self

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Vector(*list(x * other for x in self.coords))
        if isinstance(other, Vector):
            return sum(x * y for x, y in zip(self.coords, other.coords))
        raise NotImplementedError("Not supported to mul non-(Vector or float) and Vector")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return abs(self.x - other.x) < EPSILON and abs(self.y - other.y) < EPSILON

    def to_int(self):
        return Vector(*(int(i) for i in self.coords))

    def is_null(self):
        return self == Vector.NULL_VECTOR

    def angle(self, other: __name__):
        if not (self.is_null() or other.is_null()):
            return acos(self * other / (abs(self) * abs(other)))

    def copy(self) -> __name__:
        vector = Vector()
        for i in self.coords:
            vector.coords.append(i)
        return vector

    def normalize(self) -> __name__:
        vector = self.copy()
        mul = abs(vector)
        if not vector.is_null():
            scale = 1 / mul
            return vector * scale
        return vector


Vector.NULL_VECTOR = Vector(0.0, 0.0)
