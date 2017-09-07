from math import cos, sin, pi

from kappa.core.geom import Point, Angle, Vector


class Circle:
    def __init__(self, center, radius: float):
        self.center: Point = center
        self.radius: float = radius

    def __call__(self, t: float = 0, speed: float = 1, phi0: Angle = Angle(0)) -> Point:
        phi = phi0 + Angle(speed * t / self.radius)
        return Point(self.radius * cos(phi.angle), self.radius * sin(phi.angle))

    def get_angle(self, p: Point) -> Angle:
        v: Vector = p - self.center
        v_r: Vector = Vector(1, 0)
        a: float = v * v_r / abs(v)
        if v.y < 0:
            a = 2 * pi - a
        return Angle(a)
