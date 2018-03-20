from kappa.common.object.GameObject import GameObject
from kappa.common.texture.TextureController import TextureController


class StateTextureController(TextureController):
    def __init__(self):
        self.__texture_holder = {}

    def __getitem__(self, key):
        return self.__texture_holder[key]

    def __setitem__(self, key, value):
        self.__texture_holder[key] = value

    def __delitem__(self, key):
        del self.__texture_holder[key]

    def get_textures(self, obj: GameObject):
        return self[obj.state]
