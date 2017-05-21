import pygame
import os


class Instance:
    def __init__(self, caption=None):
        self.caption = caption
        self.clock = None
        self.screen = None
        self.keyboard_link = None

    def init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.caption)

    def link_keyboard_object(self, obj):
        self.keyboard_link = obj

    def start(self):
        while 1:
            self.clock.tick(100)
            for event in pygame.event.get():
                if not self.parse_event(event):
                    return

            self.update()

            self.screen.blit()

            pygame.display.flip()

    def parse_event(self, event):
        pass

    def update(self):
        pass
