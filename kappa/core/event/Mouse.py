import pygame


class Mouse:
    @staticmethod
    def get_pressed():
        return pygame.mouse.get_pressed()

    @staticmethod
    def set_visible(visible):
        return pygame.mouse.set_visible(visible)
