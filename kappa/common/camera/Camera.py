from ...Settings import CAMERA_DEFAULT_WIDTH, CAMERA_DEFAULT_HEIGHT
from ..object.RectShape import RectShape
from ..object.GameObject import GameObject
from ..object.SimpleMovingStrategy import SimpleMovingStrategy
from ...core.geom.Point import Point


class Camera(GameObject):
    def __init__(self, center=Point(0, 0, 0)):
        GameObject.__init__(self,
                            center,
                            None,
                            RectShape(CAMERA_DEFAULT_WIDTH,
                                      CAMERA_DEFAULT_HEIGHT,
                                      ),
                            SimpleMovingStrategy()
                            )
