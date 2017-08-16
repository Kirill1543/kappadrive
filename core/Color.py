import pygame


class Color(pygame.Color):
    def __init__(self, r, g, b):
        pygame.Color.__init__(r, g, b)
