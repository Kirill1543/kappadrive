from kappa.common.object.shape.Shape import Shape
from kappa.core.Color import BLACK
from kappa.core.frame.Frame import Frame
from kappa.core.primitives.Draw import Draw


class RectShape(Shape):
    def __init__(self, width, height, color=BLACK):
        super().__init__(color)
        self.__width = width
        self.__height = height
        self.__shape: Frame = self.__create_shape()

    def __create_shape(self) -> Frame:
        center = (self.width // 2, self.height // 2)
        frame = Frame((self.width, self.height))
        ck = (127, 33, 33)
        frame.surface.fill(ck)
        frame.surface.set_colorkey(ck)
        frame.surface.set_at(center, self.color)
        Draw.rect(frame, self.color, (0, 0), (self.width, self.height), 1)
        return frame

    @property
    def shape(self) -> Frame:
        return self.__shape

    @property
    def width(self) -> float:
        return self.__width

    @property
    def height(self) -> float:
        return self.__height

    @property
    def is_rect(self) -> bool:
        return True
