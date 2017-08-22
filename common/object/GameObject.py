from kappa.core.frame import Frame
from kappa.core.geom.Point import Point
from kappa.core.geom.Vector import Vector
from kappa.logger.Logger import Logger
from .CommonObject import CommonObject


class GameObject(CommonObject):
    log = Logger(__name__).get()

    def __init__(self, center: Point, texture, shape, moving_style):
        CommonObject.__init__(self, center, texture)
        self._shape = shape
        self._m = moving_style

    def update(self):
        pass

    def start_move(self, direction):
        self._m.change_move(direction, 1)

    def stop_move(self, direction):
        self._m.change_move(direction, -1)

    def move(self):
        self._m.move(self.center)

    def draw_shape_on(self, main_frame: Frame, center: Point, color):
        topleft = (int(center.x - self.width / 2), int(center.y - self.height / 2))
        GameObject.log.debug("Adding texture in {}".format(topleft))
        main_frame.display(self._shape.get_shape(color), topleft)

    @property
    def width(self):
        return self._shape.width

    @property
    def height(self):
        return self._shape.height

    @property
    def x(self):
        return self.center.x - self._shape.width // 2

    @x.setter
    def x(self, value):
        self.center.x = value + self._shape.width // 2

    @property
    def y(self):
        return self.center.y - self._shape.height // 2

    @y.setter
    def y(self, value):
        self.center.y = value + self._shape.height // 2

    @property
    def topleft(self):
        return Point(self.x, self.y, 0)

    @property
    def move_vector(self):
        return self._m.move_vector

    @move_vector.setter
    def move_vector(self, value: Vector):
        self._m.move_vector = value
