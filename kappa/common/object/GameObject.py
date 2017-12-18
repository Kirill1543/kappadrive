from math import sqrt

from .CommonObject import CommonObject
from .MovingStrategy import MovingStrategy
from .Shape import Shape
from ...core.frame.Frame import Frame
from ...core.geom import EPSILON
from ...core.geom import Point
from ...core.geom import Vector
from ...logger.Logger import Logger


class GameObject(CommonObject):
    log = Logger(__name__).get()

    def __init__(self, center: Point, texture, shape: Shape, moving_strategy):
        CommonObject.__init__(self, center, texture)
        self.__shape: Shape = shape
        self.__m: MovingStrategy = moving_strategy

    def update(self):
        pass

    def start_move(self, direction):
        self.__m.change_move(direction, 1)

    def stop_move(self, direction):
        self.__m.change_move(direction, -1)

    def move_offset(self, offset: Vector):
        self.center += offset

    def move(self, t=1):
        self.center += self.__m.get_time_offset(t)

    def get_time_position(self, t=1) -> Point:
        return self.center + self.__m.get_time_offset(t)

    def intersect(self, obj: __name__, t=0) -> bool:
        if self.shape.is_circle and obj.shape.is_circle:
            c: Vector = obj.center - self.center
            v: Vector = self.__m.get_time_offset(t)
            r: float = obj.shape.radius + self.__shape.radius
            d = v * c - (c * c - r * r)
            GameObject.log.debug("Calculated c={}, v={}, r={}, d={}".format(c.coords, v.coords, r, d))
            if d >= 0.0:
                return True
        return False

    def is_going_intersect(self, obj) -> bool:
        return self.intersect(obj, 1)

    def move_time_to(self, obj: __name__) -> float:
        GameObject.log.debug("Calculating moving time from {} to {}".format(self, obj))
        if self.shape.is_circle and obj.shape.is_circle:
            GameObject.log.debug("Both have Circle Shapes.")
            cc: Vector = self.center - obj.center
            v: Vector = self.move_vector
            r: float = obj.shape.radius + self.__shape.radius
            b = v * cc
            a = (v * v)
            c = (cc * cc - r * r)
            d = b * b - c * a
            GameObject.log.debug("Calculated c={}, v={}, r={}, d={}".format(cc.coords, v.coords, r, d))
            if d > EPSILON:
                d_sqrt = sqrt(d)
                roots = (-b - d_sqrt) / a, (-b + d_sqrt) / a
                GameObject.log.debug("Found roots={}; sqrt(d)={} a={} b={} c={}".format(roots, d_sqrt, a, b, c))
                if roots[1] > EPSILON:
                    return min(roots[0], 1)
        else:
            GameObject.log.debug("Even 1 of them has not a Circle Shape, skipping...")
        return 1.0

    def draw_shape_on(self, main_frame: Frame, center: Point):
        topleft = (int(center.x - self.width / 2), int(center.y - self.height / 2))
        GameObject.log.debug("Adding shape for {} in {}".format(self, topleft))
        main_frame.display(self.__shape.shape, topleft)

    @property
    def width(self):
        return self.__shape.width

    @property
    def height(self):
        return self.__shape.height

    @property
    def x(self):
        return self.center.x - self.__shape.width // 2

    @x.setter
    def x(self, value):
        self.center.x = value + self.__shape.width // 2

    @property
    def y(self):
        return self.center.y - self.__shape.height // 2

    @y.setter
    def y(self, value):
        self.center.y = value + self.__shape.height // 2

    @property
    def topleft(self):
        return Point(self.x, self.y, 0)

    @property
    def move_vector(self):
        return self.__m.get_time_offset()

    @move_vector.setter
    def move_vector(self, value: Vector):
        self.__m.move_vector = value

    @property
    def is_movable(self):
        return self.__m.is_movable

    @property
    def shape(self):
        return self.__shape

    @property
    def speed(self):
        return self.__m.speed

    @speed.setter
    def speed(self, value):
        self.__m.speed = value
