from ...core.frame.Frame import Frame
from ...core.primitives.Draw import Draw


class CircleShape:
    def __init__(self, r):
        self.radius = r

    def get_shape(self, color):
        center = (self.radius, self.radius)
        frame = Frame((self.radius * 2, self.radius * 2))
        ck = (127, 33, 33)
        frame.surface.fill(ck)
        frame.surface.set_colorkey(ck)
        frame.surface.set_at(center, color)
        Draw.circle(frame, color, center, self.radius, 1)
        return frame

    @property
    def width(self):
        return self.radius * 2

    @property
    def height(self):
        return self.radius * 2
