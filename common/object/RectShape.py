from ...common.object.Shape import Shape
from ...core.Color import BLACK
from ...core.frame.Frame import Frame
from ...core.primitives.Draw import Draw


class RectShape(Shape):
    def __init__(self, width, height, color=BLACK):
        super().__init__(color)
        self._width = width
        self._height = height
        self._shape = self._create_shape()

    def _create_shape(self) -> Frame:
        center = (self.width // 2, self.height // 2)
        frame = Frame((self.width, self.height))
        ck = (127, 33, 33)
        frame.surface.fill(ck)
        frame.surface.set_colorkey(ck)
        frame.surface.set_at(center, self.color)
        Draw.rect(frame, self.color, (0, 0), (self.width, self.height), 1)
        return frame

    @property
    def shape(self):
        return self._shape

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def is_rect(self):
        return True
