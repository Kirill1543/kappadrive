from kappa.common.texture.Animation import Animation
from kappa.core.frame.Frame import Frame


class SingleTexture(Animation):
    def __init__(self, texture: Frame):
        Animation.__init__(self)
        self.__texture: Frame = texture

    def get(self) -> Frame:
        return self.__texture
