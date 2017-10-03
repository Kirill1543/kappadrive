import pygame

from ..geom import Point


class Draw:
    @staticmethod
    def circle(frame, color, pos: Point, radius, width=0):
        pygame.draw.circle(frame.surface, color, pos.to_int().coords[:2], radius, width)

    @staticmethod
    def rect(frame, color, topleft, size, width=0):
        pygame.draw.rect(frame.surface, color, pygame.Rect(topleft, size), width)

    @staticmethod
    def line(frame, color, start: Point, end: Point, width=1):
        pygame.draw.line(frame.surface, color, start.to_int().coords[:2], end.to_int().coords[:2], width)
