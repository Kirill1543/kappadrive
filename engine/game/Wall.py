import pygame
from engine.common.object.RectObject import RectObject


class Wall(RectObject):
    def __init__(self, center, texture, width, height):
        RectObject.__init__(self, center, texture, width, height)

    def get_img(self):
        return None
