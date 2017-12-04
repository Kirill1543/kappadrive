import pygame

from ...core.frame.Frame import Frame


class Transform:
    @staticmethod
    def scale_to(frame, size):
        pygame.transform.scale(frame.surface, size)

    @staticmethod
    def copy_from(image, x, y, w, h, w_fin=None, h_fin=None):
        w_fin = w_fin or w
        h_fin = h_fin or h
        return Frame((w_fin, h_fin)).display(
            Transform.scale_to(image.subframe(x, y, w, h), (w_fin, h_fin)), (0, 0))
