from ...Settings import SCREEN_DEFAULT_WIDTH, SCREEN_DEFAULT_HEIGHT
from ..object.RectShape import RectShape
from ..object.GameObject import GameObject
from ..object.SimpleMovingStrategy import SimpleMovingStrategy
from ...core.geom.Point import Point


class Camera(GameObject):
    def __init__(self, center=Point(0, 0, 0), w=SCREEN_DEFAULT_WIDTH, h=SCREEN_DEFAULT_HEIGHT):
        GameObject.__init__(self,
                            center,
                            None,
                            RectShape(w, h),
                            SimpleMovingStrategy()
                            )
