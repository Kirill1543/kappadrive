from ...core.frame.Frame import Frame
from ...core.primitives.Draw import Draw


class CircularObject:
    def __init__(self, r):
        self.radius = r

    def get_shape(self, color):
        size = (self.radius, self. radius)
        frame = Frame((self.radius*2, self.radius*2))
        Draw.circle(frame, color, size, self.radius, 0)
        return frame
