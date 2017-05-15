from ...Settings import Settings
from .ObjectStates import ObjectStates
from .CommonObject import CommonObject


class GameObject(CommonObject):
    def __init__(self, center, texture, shape, moving_style):
        CommonObject.__init__(self, center, texture)
        self._shape = shape
        self._m = moving_style

    def update(self):
        self.move()

    def start_move(self, direction):
        self._m.change_move(direction, 1)

    def stop_move(self, direction):
        self._m.change_move(direction, -1)

    def move(self):
        self._m.move(self.center)

    def draw(self, x, y, color, screen):
        self._shape.draw(x, y, color, screen)

    @property
    def width(self):
        return self._shape.width

    @property
    def height(self):
        return self._shape.height

    @property
    def x(self):
        return self.center.x - self._shape.width / 2

    @x.setter
    def x(self, value):
        self.center.x = value + self._shape.width / 2

    @property
    def y(self):
        return self.center.y - self._shape.height / 2

    @y.setter
    def y(self, value):
        self.center.y = value + self._shape.height / 2