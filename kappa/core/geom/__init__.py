from copy import copy

from math import sqrt

from ...logger.Logger import Logger

EPSILON = 0.000001

from .Coordinates import Coordinates
from .Vector import Vector
from .Angle import Angle
from .Point import Point
from .Circle import Circle
from .Line import Line

__all__ = ["Vector", "Circle", "Point", "Coordinates", "Line", "Angle", "O", "intersection_circle_with_circle",
           "EPSILON"]

O = Point(0, 0)

log = Logger(__name__).get()


def intersection_line_with_circle(line: Line, circle: Circle) -> list:
    log.debug("Calculating Line(a={},b={},c={}) and Circle(c={},r={}) Intersection".format(line.a, line.b, line.c,
                                                                                           circle.center,
                                                                                           circle.radius))
    l: Line = copy(line).move(O - circle.center)
    vv: float = l.a ** 2 + l.b ** 2
    c_vv: float = l.c / vv
    c0: Point = Point(- l.a * c_vv, -l.b * c_vv)
    r = circle.radius
    d: float = r * r - l.c * c_vv
    log.debug("Calculated: median={}, r={}".format(sqrt(l.c * c_vv), r))
    log.debug("Calculated: v^2={}, c_vv={}, c0={}, r={}, d^2={}".format(vv, c_vv, c0, r, d))
    if d < 0.0:
        log.debug("Found 0 roots")
        return []
    elif abs(d) < EPSILON:
        log.debug("Found 1 root:{}".format(c0))
        return [c0]
    else:
        m: float = sqrt(d / vv)
        v = Vector(l.b, -l.a)
        roots = [c0 - v * m, c0 + v * m]
        log.debug("Found 2 roots:{}".format(roots))
        return roots


def intersection_circle_with_circle(c1: Circle, c2: Circle) -> list:
    log.debug("Calculating Circle(c={},r={}) and Circle(c={},r={}) Intersection".format(c1.center, c1.radius, c2.center,
                                                                                        c2.radius))
    c0: Point = c2.center - c1.center
    c: Circle = Circle(O, c1.radius)
    l: Line = Line(a=-2 * c0.x, b=-2 * c0.y, c=c0.x ** 2 + c0.y ** 2 + c1.radius ** 2 - c2.radius ** 2)
    return [i + (c1.center - O) for i in intersection_line_with_circle(l, c)]
