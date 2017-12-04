from . import Coordinates, Vector


class Point(Coordinates):
    def __init__(self, *args):
        super().__init__(*args)

    def __neg__(self):
        return Point(*list(-x for x in self.coords))

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("Not supported to add non-Vector to Point")
        return Point(*list(x + y for x, y in zip(self.coords, other.coords)))

    def __sub__(self, other):
        if not isinstance(other, Coordinates):
            raise NotImplementedError("Not supported to sub non-Coordinate from Point")
        return dict(Vector=Point, Point=Vector)[other.__class__.__name__](
            *list(x - y for x, y in zip(self.coords, other.coords)))

    def __iadd__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("Not supported to iadd non-Vector to Point")
        self.coords = list(x + y for x, y in zip(self.coords, other.coords))
        return self

    def __isub__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("Not supported to isub non-Vector from Point")
        self.coords = list(x - y for x, y in zip(self.coords, other.coords))
        return self

    def to_int(self):
        return Point(*(int(i) for i in self.coords))
