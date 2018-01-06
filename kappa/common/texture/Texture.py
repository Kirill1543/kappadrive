from ...core.frame.Frame import Frame


class Texture:
    def __init__(self, frame: Frame):
        self.__source: Frame = frame

    def get(self) -> Frame:
        return self.__source
