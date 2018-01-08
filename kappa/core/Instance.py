import timeit

import pygame
from pygame.time import Clock

from ..common.screen.Screen import Screen
from ..logger.Logger import Logger


class Instance:
    log = Logger(__name__).get()

    def __init__(self, caption: str = 'kappa game'):
        self.caption: str = caption
        self.clock: Clock = None
        self.screen: Screen = None

    def init(self):
        pygame.init()
        self.clock = Clock()
        pygame.display.set_caption(self.caption)

    def start(self):
        while 1:
            Instance.log.debug("Instance update iteration started")
            start_time = timeit.default_timer()
            self.clock.tick(100)
            for event in pygame.event.get():
                if not self.parse_event(event):
                    return

            self.update()
            self.screen.display()

            pygame.display.flip()
            Instance.log.debug("Instance update iteration finished:")
            Instance.log.debug("Total execution time={}ms".format((timeit.default_timer() - start_time) * 1000))

    def parse_event(self, event):
        pass

    def update(self):
        start_time = timeit.default_timer()
        self.screen.update()
        Instance.log.debug("Screen updating time={}ms".format((timeit.default_timer() - start_time) * 1000))
