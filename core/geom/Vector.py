from kappa.core.geom.Coordinates import Coordinates


class Vector(Coordinates):
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
