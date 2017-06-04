import pygame


class Draw:
    @staticmethod
    def circle(frame, color, pos, radius, width):
        pygame.draw.circle(frame.surface, color, pos, radius, width)
