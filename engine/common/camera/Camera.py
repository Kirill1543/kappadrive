from engine.Settings import Settings
from engine.common.object.RectObject import RectObject
from engine.common.object.GameObject import GameObject
from engine.common.object.MovingObject import MovingObject
from engine.common.object.Point import Point


class Camera(RectObject, GameObject):
    def __init__(self, center=Point(0, 0, 0)):
        RectObject.__init__(self, center, None, Settings.CAMERA_DEFAULT_WIDTH, Settings.CAMERA_DEFAULT_HEIGHT)
        GameObject.__init__(self, MovingObject())
