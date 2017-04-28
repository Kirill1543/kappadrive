from engine.Settings import Settings
from engine.common.object.ObjectStates import ObjectStates
from engine.common.object.CommonObject import CommonObject


class GameObject(CommonObject):
    def __init__(self, center, texture, shape, moving_style):
        CommonObject.__init__(self, center, texture)
        self._shape = shape
        self._m = moving_style

    def update(self):
        self.move()

    def move(self):
        self._m.move()
