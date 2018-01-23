import pygame

from .Frame import Frame


class FrameHelper:
    @staticmethod
    def scale_to(frame, size) -> Frame:
        return Frame.by_surface(pygame.transform.scale(frame.surface, size))

    @staticmethod
    def copy_from(image, x, y, w, h, w_fin=None, h_fin=None) -> Frame:
        w_fin = w_fin or w
        h_fin = h_fin or h
        return FrameHelper.scale_to(image.subframe(x, y, w, h), (w_fin, h_fin))
