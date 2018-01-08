from ..object.Shape import Shape
from ...core.Color import BLACK
from ...core.geom import Point
from ...core.frame.Frame import Frame
from ...core.primitives.Draw import Draw


class CircleShape(Shape):
    def __init__(self, r, color=BLACK):
        super().__init__(color)
        self.__radius = r
        self.__shape: Frame = self.__create_shape()

    def __create_shape(self) -> Frame:
        center = (self.radius, self.radius)
        frame = Frame((self.radius * 2, self.radius * 2))
        ck = (127, 33, 33)
        frame.surface.fill(ck)
        frame.surface.set_colorkey(ck)
        frame.surface.set_at(center, self.color)
        Draw.circle(frame, self.color, Point(*center), self.radius, 1)
        return frame

    @property
    def shape(self) -> Frame:
        return self.__shape

    @property
    def width(self) -> float:
        return self.__radius * 2

    @property
    def height(self) -> float:
        return self.__radius * 2

    @property
    def radius(self) -> float:
        return self.__radius

    @property
    def is_circle(self) -> bool:
        return True
