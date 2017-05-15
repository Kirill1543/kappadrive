import pygame


# Interface
class RectObject:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, x, y, color, screen):
        pass
