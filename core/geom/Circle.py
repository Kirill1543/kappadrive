from math import cos, sin, pi

from ...logger.Logger import Logger
from . import Point, Angle, Vector


class Circle:
    log = Logger(__name__).get()

    def __init__(self, center, radius: float):
        self.center: Point = center
        self.radius: float = radius

    def __call__(self, t: float = 0, speed: float = 1, phi0: Angle = Angle(0)) -> Point:
        phi = phi0 + Angle(speed * t / self.radius)
        return Point(self.radius * cos(phi.angle), self.radius * sin(phi.angle))

    def __str__(self):
        return "{}({}:{})".format(self.__class__.__name__, self.center, self.radius)

    def get_angle(self, p: Point) -> Angle:
        v: Vector = p - self.center
        v_r: Vector = Vector(1, 0)
        a: float = v * v_r / abs(v)
        if v.y < 0:
            a = 2 * pi - a
        return Angle(a)

    def get_tangent_points(self, v: Vector) -> list:
        Circle.log.debug("Calculating tangent points for {} with {}".format(self, v))
        v_orth = Vector(v.y, -v.x).normalize() * self.radius
        points = [self.center - v_orth, self.center + v_orth]
        Circle.log.debug("Found tangent points: {}".format(points))
        return points
