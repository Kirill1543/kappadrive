import pygame


# Interface
class CircularObject:
    def __init__(self, r):
        self.radius = r

    def draw(self, x, y, color, screen):
        pygame.draw.circle(screen, color, (int(x), int(y)), self.radius, 0)
