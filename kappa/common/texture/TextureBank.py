import os


class TextureBank:
    def __init__(self):
        self.__src_path: str = ''
        self.__bank: dict = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__bank[key] = value

    def __delitem__(self, key):
        del self.__bank[key]

    def load(self, path: os.path):
        self.__src_path = path
