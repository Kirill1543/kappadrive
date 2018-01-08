from ..frame.Frame import Frame
from ..frame.Transform import Transform
import pygame


class Image:
    @staticmethod
    def load(path):
        return Frame.by_surface(pygame.image.load(path))

    @staticmethod
    def load_packed(full_path, width, height, source_width, source_height):
        image = Image.load(full_path)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()

        loaded_images = []

        count_width = image.get_rect().width // source_width
        count_height = image.get_rect().heght // source_height

        for j in range(0, count_height):
            for i in range(0, count_width):
                loaded_images.append(
                    Transform.copy_from(image, i * source_width, j * source_height, source_width, source_height, width,
                                        height))

        return loaded_images
