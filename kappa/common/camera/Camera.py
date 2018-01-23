from ..object.GameObject import GameObject
from ..object.RectShape import RectShape
from ..object.MovableUpdateStrategy import MovableUpdateStrategy
from ...core.geom.Point import Point


class Camera(GameObject):
    def __init__(self, w=0, h=0, center=Point(0, 0, 0)):
        GameObject.__init__(self,
                            center,
                            RectShape(w, h),
                            MovableUpdateStrategy()
                            )
