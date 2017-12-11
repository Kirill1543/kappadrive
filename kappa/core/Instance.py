import timeit

import pygame
from pygame.time import Clock

from ..common.object.GameObject import GameObject
from ..common.screen.Screen import Screen
from ..logger.Logger import Logger


class Instance:
    log = Logger(__name__).get()

    def __init__(self, caption: str = None):
        self.caption: str = caption
        self.clock: Clock = None
        self.screen: Screen = None
        self.keyboard_link: GameObject = None

    def init(self):
        pygame.init()
        self.clock = Clock()
        pygame.display.set_caption(self.caption)

    def link_keyboard_object(self, obj):
        self.keyboard_link = obj

    def start(self):
        while 1:
            Instance.log.debug("Starting Game Instance update iteration")
            start_time = timeit.default_timer()
            self.clock.tick(100)
            for event in pygame.event.get():
                if not self.parse_event(event):
                    return

            self.update()
            Instance.log.debug("Player Position:{}".format(self.keyboard_link.center.coords))
            self.screen.camera.center_on(self.keyboard_link)
            self.screen.display()

            pygame.display.flip()
            Instance.log.debug("Total execution time={}ms".format((timeit.default_timer() - start_time) * 1000))

    def parse_event(self, event):
        pass

    def update(self):
        pass
