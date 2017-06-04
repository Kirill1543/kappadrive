from .Frame import Frame


class FrameFactory:
    @staticmethod
    def by_surface(surface):
        frame = Frame()
        frame.surface = surface
        return frame

    @staticmethod
    def empty(size=(0, 0)):
        return Frame(size)
