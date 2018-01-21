import os

from kappa.core.image.Image import Image
from kappa.system.meta.Singleton import Singleton


class TextureManager(metaclass=Singleton):
    PACK_TAG = 'pack'

    def __init__(self):
        self.__src_path: str = None
        self.__texture_holder: dict = {}

    def __getitem__(self, key):
        return self.__texture_holder[key]

    def __setitem__(self, key, value):
        self.__texture_holder[key] = value

    def __delitem__(self, key):
        del self.__texture_holder[key]

    def load(self, path: os.path):
        self.__src_path = path
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isfile(full_path):
                item_without_extension = item.split('.')[0]
                if item.startswith(TextureManager.PACK_TAG):
                    pack_tag, size, item_without_extension = item_without_extension.split('_')
                    self.__texture_holder[item_without_extension] = Image.load_packed(full_path, int(size), int(size))
                else:
                    self.__texture_holder[item_without_extension] = Image.load(full_path)
