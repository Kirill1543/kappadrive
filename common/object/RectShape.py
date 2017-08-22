from kappa.core.frame.Frame import Frame
from kappa.core.primitives.Draw import Draw


class RectShape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_shape(self, color):
        center = (self.width // 2, self.height // 2)
        frame = Frame((self.width, self.height))
        ck = (127, 33, 33)
        frame.surface.fill(ck)
        frame.surface.set_colorkey(ck)
        frame.surface.set_at(center, color)
        Draw.rect(frame, color, (0, 0), (self.width, self.height), 1)
        return frame
