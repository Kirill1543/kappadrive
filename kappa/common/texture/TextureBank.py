import os
import pygame

from kappa.core.image.Image import Image
from ...Settings import BACKGROUND_TEXTURE_WIDTH, BACKGROUND_TEXTURE_HEIGHT, BACKGROUND_TEXTURE_SOURCE_WIDTH, \
    BACKGROUND_TEXTURE_SOURCE_HEIGHT
from ...core.frame.Frame import Frame


class TextureBank:
    def __init__(self):
        self.__src_path: str = None
        self.__bank: dict = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __getitem__(self, key):
        return self.__bank[key]

    def __setitem__(self, key, value):
        self.__bank[key] = value

    def __delitem__(self, key):
        del self.__bank[key]

    def load(self, path: os.path):
        self.__src_path = path
        for item in os.listdir(path):
            if os.path.isfile(path):
                item_without_extension = item.split('.')
                self.__bank[item_without_extension] = Image.load_packed(os.path.join(path, item))
