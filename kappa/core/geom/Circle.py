import math

from . import Point, Angle, Vector, Coordinates
from ...logger.Logger import Logger


class Circle:
    log = Logger(__name__).get()

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius: float = radius

    def __call__(self, t: float = 0, speed: float = 1, phi0: Angle = Angle(0)) -> Point:
        phi = phi0 + Angle(speed * t / self.radius)
        return self.center + Vector(self.radius * math.cos(phi.radians), self.radius * math.sin(phi.radians), 0)

    def __str__(self):
        return "{}({}:{})".format(self.__class__.__name__, self.center, self.radius)

    def get_tangent_points(self, v: Vector) -> list:
        Circle.log.debug("Calculating tangent points for {} with {}".format(self, v))
        v_orth = Vector(v.y, -v.x).normalize() * self.radius
        points = [self.center - v_orth, self.center + v_orth]
        Circle.log.debug("Found tangent points: {}".format(points))
        return points

    def get_angle(self, c: Coordinates) -> Angle:
        Circle.log.debug("Calculating angles for {} at {}".format(self, c))
        if isinstance(c, Point):
            return self.get_angle(self.center - c)
        elif isinstance(c, Vector):
            return Angle(math.atan2(c.y, c.x))
        else:
            raise NotImplementedError("Not implemented to get angle from non-Coordinates heir")
