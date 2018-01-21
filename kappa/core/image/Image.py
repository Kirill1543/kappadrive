from ..frame.Frame import Frame
from ..frame.FrameHelper import FrameHelper
import pygame


class Image:
    @staticmethod
    def load(path):
        image = pygame.image.load(path)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        return Frame.by_surface(image)

    @staticmethod
    def load_packed(path, source_width, source_height):
        image = Image.load(path)

        loaded_images = []

        count_width = image.get_rect().width // source_width
        count_height = image.get_rect().height // source_height

        for j in range(0, count_height):
            for i in range(0, count_width):
                loaded_images.append(
                    FrameHelper.copy_from(image, i * source_width, j * source_height, source_width, source_height))

        return loaded_images
