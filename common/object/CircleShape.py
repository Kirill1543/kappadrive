from kappa.common.object.Shape import Shape
from kappa.core.Color import BLACK
from kappa.core.geom import Point
from ...core.frame.Frame import Frame
from ...core.primitives.Draw import Draw


class CircleShape(Shape):
    def __init__(self, r, color=BLACK):
        super().__init__(color)
        self._radius = r
        self._shape = self._create_shape()

    def _create_shape(self) -> Frame:
        center = (self.radius, self.radius)
        frame = Frame((self.radius * 2, self.radius * 2))
        ck = (127, 33, 33)
        frame.surface.fill(ck)
        frame.surface.set_colorkey(ck)
        frame.surface.set_at(center, self.color)
        Draw.circle(frame, self.color, Point(*center), self.radius, 1)
        return frame

    @property
    def shape(self):
        return self._shape

    @property
    def width(self):
        return self.radius * 2

    @property
    def height(self):
        return self.radius * 2

    @property
    def radius(self):
        return self._radius

    @property
    def is_circle(self):
        return True
