from kappa.core.geom import Point
from kappa.core.geom import Vector


class Line:
    def __init__(self, **kwargs):
        keys = kwargs.keys()
        if 'from' in keys:
            from_point: Point = kwargs.get('from')
            vector: Vector = kwargs.get('vector', None)
            if 'to' in keys:
                vector = kwargs.get('to') - from_point
            self.a = vector.y
            self.b = -vector.x
            self.c = from_point.y * vector.x - from_point.x * vector.y
        else:
            self.a = kwargs.get('a', 0)
            self.b = kwargs.get('b', 0)
            self.c = kwargs.get('c', 0)

    def __copy__(self):
        return Line(a=self.a, b=self.b, c=self.c)

    def move(self, vector: Vector):
        self.c = Vector(self.a, self.b, self.c) * Vector(-vector.x, -vector.y, 1)
        return self
