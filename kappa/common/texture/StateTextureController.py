from kappa.common.object.State import State
from kappa.common.texture.TextureController import TextureController


class StateTextureController(TextureController):
    def __init__(self):
        self.__texture_holder = {}

    def __getitem__(self, key: State):
        return self.__texture_holder[key]

    def __setitem__(self, key: State, value):
        self.__texture_holder[key] = value

    def __delitem__(self, key: State):
        del self.__texture_holder[key]
