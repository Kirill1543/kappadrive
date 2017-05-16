import pygame
from pygame.locals import *
import os


class Instance:
    def __int__(self):
        self.caption = None
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
            # Make sure game doesn't run at more than 60 frames per second
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.keyboard_link.start_move(u'UP')
                    if event.key == K_DOWN:
                        self.keyboard_link.start_move(u'DOWN')
                    if event.key == K_LEFT:
                        self.keyboard_link.start_move(u'LEFT')
                    if event.key == K_RIGHT:
                        self.keyboard_link.start_move(u'RIGHT')
                elif event.type == KEYUP:
                    if event.key == K_UP:
                        self.keyboard_link.stop_move(u'UP')
                    if event.key == K_DOWN:
                        self.keyboard_link.stop_move(u'DOWN')
                    if event.key == K_LEFT:
                        self.keyboard_link.stop_move(u'LEFT')
                    if event.key == K_RIGHT:
                        self.keyboard_link.stop_move(u'RIGHT')

            self.update()

            self.screen.camera.center_on(self.keyboard_link)
            self.screen.blit()

            pygame.display.flip()

    def parse_event(self):
        pass

    def update(self):
        pass
