from engine.Settings import Settings
from engine.common.object.RectObject import RectObject
from engine.common.object.GameObject import GameObject
from engine.common.object.MovingObject import MovingObject
from engine.common.object.Point import Point


class Camera(GameObject):
    def __init__(self, center=Point(0, 0, 0)):
        GameObject.__init__(self, center, None,
                            RectObject(Settings.CAMERA_DEFAULT_WIDTH, Settings.CAMERA_DEFAULT_HEIGHT), MovingObject())
