import pygame
from .FrameFactory import FrameFactory


class Frame:
    def __init__(self, size=(0, 0), flags=0, depth=0, masks=None):
        self._surface = pygame.Surface(size, flags, depth, masks)

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, value):
        self._surface = value

    def display(self, source, dest, area=None, special_flags=0):
        self._surface.blit(source.surface, dest, area, special_flags)

    def get_alpha(self):
        return self._surface.get_alpha()

    def convert(self):
        return FrameFactory.by_surface(self._surface.convert())

    def convert_alpha(self):
        return FrameFactory.by_surface(self._surface.convert_alpha())

    def get_rect(self):
        return self._surface.get_rect()

    def subframe(self, x, y, w, h):
        return FrameFactory.by_surface(self._surface.subsurface(x, y, w, h))
