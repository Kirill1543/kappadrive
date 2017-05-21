import pygame


class LoadImage:
    @staticmethod
    def load_image(full_path):
        pygame.image.load(full_path)

    @staticmethod
    def empty_image(w, h):
        return pygame.Surface(w, h)

    @staticmethod
    def scale_to(image, size):
        pygame.transform.scale(image, size)

    @staticmethod
    def crop(image, x, y, w, h):
        return image.subsurface(x, y, w, h)

    @staticmethod
    def copy_from(image, x, y, w, h, w_fin=None, h_fin=None):
        w_fin = w_fin or w
        h_fin = h_fin or h
        return LoadImage.empty_image(w_fin, h_fin).blit(
            LoadImage.scale_to(LoadImage.crop(image, x, y, w, h), (w_fin, h_fin)), (0, 0))
