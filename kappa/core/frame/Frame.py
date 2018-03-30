import pygame


class Frame:
    def __init__(self, size=(0, 0), flags=0, depth=0, masks=None):
        self.__surface = pygame.Surface(size)

    @staticmethod
    def set_mode(size, flags=0, depth=0):
        return Frame.by_surface(pygame.display.set_mode(size, flags, depth))

    @property
    def surface(self):
        return self.__surface

    @surface.setter
    def surface(self, value):
        self.__surface = value

    def display(self, source, dest, area=None, special_flags=0):
        self.__surface.blit(source.surface, dest, area, special_flags)

    def get_alpha(self):
        return self.__surface.get_alpha()

    def convert(self):
        return Frame.by_surface(self.__surface.convert())

    def convert_alpha(self):
        return Frame.by_surface(self.__surface.convert_alpha())

    def get_rect(self):
        return self.__surface.get_rect()

    def subframe(self, x, y, w, h):
        return Frame.by_surface(self.__surface.subsurface(x, y, w, h))

    def get_size(self):
        return self.__surface.get_size()

    def fill(self, color):
        self.__surface.fill(color)

    @staticmethod
    def by_surface(surface):
        frame = Frame()
        frame.surface = surface
        return frame

    @staticmethod
    def empty(size=(0, 0)):
        return Frame(size)
