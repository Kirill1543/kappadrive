from ...Settings import Settings
from ..object.RectObject import RectObject
from ..object.GameObject import GameObject
from ..object.MovingObject import MovingObject
from ..object.Point import Point


class Camera(GameObject):
    def __init__(self, center=Point(0, 0, 0)):
        GameObject.__init__(self,
                            center,
                            None,
                            RectObject(Settings.CAMERA_DEFAULT_WIDTH,
                                       Settings.CAMERA_DEFAULT_HEIGHT),
                            MovingObject()
                            )
