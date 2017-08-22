from ...Settings import Settings
from ..object.RectShape import RectShape
from ..object.GameObject import GameObject
from ..object.SimpleMovingStrategy import SimpleMovingStrategy
from ...core.geom.Point import Point


class Camera(GameObject):
    def __init__(self, center=Point(0, 0, 0)):
        GameObject.__init__(self,
                            center,
                            None,
                            RectShape(Settings.CAMERA_DEFAULT_WIDTH,
                                      Settings.CAMERA_DEFAULT_HEIGHT,
                                      ),
                            SimpleMovingStrategy()
                            )
