import pygame

from kappa.core.frame.Frame import Frame

pygame.font.init()


class Font:
    def __init__(self, name, size, bold=False, italic=False):
        self.__font = pygame.font.SysFont(name, size, bold, italic)

    @property
    def font(self):
        return self.__font

    def render(self, text, antialias, color, background=None) -> Frame:
        return Frame.by_surface(self.__font.render(text, antialias, color, background))
