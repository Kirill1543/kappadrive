import os

from kappa.core.image.Image import Image
from kappa.system.meta.Singleton import Singleton
from kappa.logger.Logger import Logger


class TextureManager(metaclass=Singleton):
    log = Logger(__name__).get()

    PACK_TAG = 'pack'
    PACK_DELIMITER = '_'
    PNG_FILE = 'png'
    ACCEPTED_FILE_EXTENSIONS = PNG_FILE
    EXTENSION_DELIMITER = '.'

    def __init__(self):
        TextureManager.log.debug("Initializing TextureManager")
        self.__src_path: str = None
        self.__texture_holder: dict = {}

    def __getitem__(self, key):
        return self.__texture_holder[key]

    def __setitem__(self, key, value):
        self.__texture_holder[key] = value

    def __delitem__(self, key):
        del self.__texture_holder[key]

    def load(self, path: os.path):
        TextureManager.log.debug("Loading path {}".format(path))
        self.__src_path = path
        self.__load_dir(path, self.__texture_holder)

    @staticmethod
    def __load_dir(path: os.path, texture_holder: dict):
        TextureManager.log.debug("Loading sub folder {}...".format(path))
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isfile(full_path):
                TextureManager.__load_file(full_path, item, texture_holder)
            else:
                texture_holder[item] = {}
                TextureManager.__load_dir(full_path, texture_holder[item])

    @staticmethod
    def __load_file(full_path, item, texture_holder: dict):
        TextureManager.log.debug("Loading file {}...".format(full_path))
        item_without_extension, item_extension = item.split(TextureManager.EXTENSION_DELIMITER)
        if item_extension in TextureManager.ACCEPTED_FILE_EXTENSIONS:
            if item.startswith(TextureManager.PACK_TAG):
                pack_tag, size, item_without_extension = item_without_extension.split(TextureManager.PACK_DELIMITER, 2)
                texture_holder[item_without_extension] = Image.load_packed(full_path, int(size), int(size))
            else:
                texture_holder[item_without_extension] = Image.load(full_path)
