from kappa.common.object.Shape import Shape
from kappa.core.Color import BLACK
from kappa.core.frame.Frame import Frame
from kappa.core.primitives.Draw import Draw


class RectShape(Shape):
    def __init__(self, width, height, color=BLACK):
        super().__init__(color)
        self._width = width
        self._height = height

    def get_shape(self):
        center = (self.width // 2, self.height // 2)
        frame = Frame((self.width, self.height))
        ck = (127, 33, 33)
        frame.surface.fill(ck)
        frame.surface.set_colorkey(ck)
        frame.surface.set_at(center, self.color)
        Draw.rect(frame, self.color, (0, 0), (self.width, self.height), 1)
        return frame

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
