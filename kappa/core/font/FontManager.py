import os

from kappa.core.font.Font import Font
from kappa.logger.Logger import Logger
from kappa.system.meta.Singleton import Singleton


class FontManager(metaclass=Singleton):
    log = Logger(__name__).get()

    TTF = 'ttf'
    ACCEPTED_FILE_EXTENSIONS = TTF
    EXTENSION_DELIMITER = '.'

    def __init__(self):
        FontManager.log.debug("Initializing FontManager")
        self.__src_path: str = None
        self.__font_holder: dict = {}

    def __getitem__(self, key):
        return self.__font_holder[key]

    def __setitem__(self, key, value):
        self.__font_holder[key] = value

    def __delitem__(self, key):
        del self.__font_holder[key]

    def load(self, path: os.path):
        FontManager.log.debug("Loading path {}".format(path))
        self.__src_path = path
        self.__load_dir(path, self.__font_holder)

    def __load_dir(self, path: os.path, font_holder: dict):
        FontManager.log.debug("Loading sub folder {}...".format(path))
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isfile(full_path):
                self.__load_file(full_path, item, font_holder)
            else:
                font_holder[item] = {}
                self.__load_dir(full_path, font_holder[item])

    def __load_file(self, full_path, item, font_holder: dict):
        FontManager.log.debug("Loading file {}...".format(full_path))
        item_without_extension, item_extension = item.split(self.EXTENSION_DELIMITER)
        if item_extension in self.ACCEPTED_FILE_EXTENSIONS:
            font_holder[item_without_extension] = lambda size: Font.from_file(full_path, size)
