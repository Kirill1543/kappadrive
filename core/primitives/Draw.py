import pygame

from kappa.core.geom.Point import Point


class Draw:
    @staticmethod
    def circle(frame, color, pos, radius, width=0):
        pygame.draw.circle(frame.surface, color, pos, radius, width)

    @staticmethod
    def rect(frame, color, topleft, size, width=0):
        pygame.draw.rect(frame.surface, color, pygame.Rect(topleft, size), width)

    @staticmethod
    def line(frame, color, start: Point, end: Point, width=1):
        pygame.draw.line(frame.surface, color, start.coords[:2], end.coords[:2], width)
