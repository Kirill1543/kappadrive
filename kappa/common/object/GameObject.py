from math import sqrt

from kappa.common.object.action.Action import Action
from kappa.common.object.action.ActionHandler import ActionHandler
from kappa.common.object.shape.Shape import Shape
from kappa.common.texture.Animation import Animation
from kappa.common.texture.TextureController import TextureController
from ...core.frame.Frame import Frame
from ...core.geom import EPSILON
from ...core.geom import Point
from ...core.geom import Vector
from ...logger.Logger import Logger


class GameObject:
    log = Logger(__name__).get()

    def __init__(self, **kwargs):
        self.center: Point = kwargs['center']
        self.__shape: Shape = kwargs['shape']
        self.__texture_controller = None
        self.__action_handler = None
        self.textures: Animation = None
        self.move_vector_normalized = Vector(0, 0)
        if 'texture_controller' in kwargs.keys():
            self.__texture_controller: TextureController = kwargs['texture_controller']
            self.textures = self.__texture_controller.get_textures(self)
        if 'action_handler' in kwargs.keys():
            self.__action_handler: ActionHandler = kwargs['action_handler']
        if 'texture_offset' in kwargs.keys():
            self.__texture_offset = kwargs['texture_offset']
        elif self.textures:
            texture_size = self.texture.get_size()
            self.__texture_offset = Vector(*[texture_size[i] // 2 for i in range(2)])

    def __str__(self) -> str:
        return "{}:{}".format(self.__class__.__name__, self.center.coords)

    def __repr__(self):
        return self.__str__()

    def center_on(self, c_obj: __name__):
        self.move_to(c_obj.center)

    def move_to(self, point: Point):
        self.center = point

    def update(self):
        GameObject.log.debug("Updating {}".format(self))
        self.textures.update()

    def handle(self, action: Action, **kwargs):
        GameObject.log.debug("{}: Handling {}".format(self, action))
        if self.__action_handler:
            self.__action_handler.handle(self, action, **kwargs)
        else:
            action.execute(self, kwargs)

    def move(self, t=1):
        self.center = self.get_time_position(t)

    def get_time_position(self, t=1) -> Point:
        return self.center + self.move_vector * t

    def intersect(self, obj: __name__, t=0) -> bool:
        if self.shape.is_circle and obj.shape.is_circle:
            c: Vector = obj.center - self.center
            v: Vector = self.move_vector * t
            r: float = obj.shape.radius + self.__shape.radius
            d = v * c - (c * c - r * r)
            GameObject.log.debug("Calculated c={}, v={}, r={}, d={}".format(c.coords, v.coords, r, d))
            if d >= 0.0:
                return True
        return False

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
        return Point(self.x, self.y)

    @property
    def texture_topleft(self):
        return self.center - self.__texture_offset

    @property
    def texture(self) -> Frame:
        return self.textures.get()

    @property
    def move_vector(self):
        return self.move_vector_normalized * self.speed

    @property
    def is_movable(self) -> bool:
        return hasattr(self, 'speed')

    @property
    def shape(self):
        return self.__shape

    @property
    def texture_controller(self):
        return self.__texture_controller

    @texture_controller.setter
    def texture_controller(self, value):
        self.__texture_controller = value

    @property
    def action_handler(self):
        return self.__action_handler

    @action_handler.setter
    def action_handler(self, value):
        self.__action_handler = value
