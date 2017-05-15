import pygame
from ...Settings import Settings


class Box(object):
    def __init__(self, background):
        self.object_list = []
        self.background = background

    def get_img(self, textures):
        img = pygame.Surface((Settings.BOX_WIDTH, Settings.BOX_HEIGHT))
        for i in range(Settings.BOX_TEXTURE_HEIGHT):
            for j in range(Settings.BOX_TEXTURE_WIDTH):
                img.blit(textures[self.background[i][j]], (j * Settings.BACKGROUND_TEXTURE_WIDTH, i * Settings.BACKGROUND_TEXTURE_HEIGHT))
        return img
