import pygame

from kappa.core.frame.Frame import Frame

pygame.font.init()


class Font:
    def __init__(self, font):
        self.__font = font

    @property
    def font(self):
        return self.__font

    def render(self, text, antialias, color, background=None) -> Frame:
        return Frame.by_surface(self.__font.render(text, antialias, color, background))

    @staticmethod
    def from_system(name, size, bold=False, italic=False):
        return __class__(pygame.font.SysFont(name, size, bold, italic))

    @staticmethod
    def from_file(path, size):
        return __class__(pygame.font.Font(path, size))
