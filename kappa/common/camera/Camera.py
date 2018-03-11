from kappa.common.object.shape.RectShape import RectShape
from kappa.common.object.update.MovableUpdateStrategy import MovableUpdateStrategy
from ..object.GameObject import GameObject
from ...core.geom.Point import Point


class Camera(GameObject):
    def __init__(self, w=0, h=0, center=Point(0, 0, 0)):
        GameObject.__init__(self,
                            center,
                            RectShape(w, h),
                            MovableUpdateStrategy()
                            )
