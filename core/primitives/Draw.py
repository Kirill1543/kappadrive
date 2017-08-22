import pygame


class Draw:
    @staticmethod
    def circle(frame, color, pos, radius, width):
        pygame.draw.circle(frame.surface, color, pos, radius, width)

    @staticmethod
    def rect(frame, color, topleft, size, width):
        pygame.draw.rect(frame.surface, color, pygame.Rect(topleft, size), width)
