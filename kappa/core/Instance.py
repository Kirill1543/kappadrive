import timeit

import pygame
from pygame.time import Clock

from ..common.screen.Screen import Screen
from ..logger.Logger import Logger


def timed(method):
    def _timed(*args, **kwargs):
        Instance.log.debug("Started {} iteration".format(method.__name__))
        start_time = timeit.default_timer()
        method(*args, **kwargs)
        Instance.log.debug(
            "Finished {} iteration. Time={}ms".format(method.__name__, (timeit.default_timer() - start_time) * 1000))

    return _timed


class Instance:
    log = Logger(__name__).get()

    def __init__(self, caption: str = 'kappa game'):
        self.caption: str = caption
        self.clock: Clock = None
        self.screen: Screen = None
        self.running = True
        self.fps = 100

    def init(self):
        pygame.init()
        self.clock = Clock()
        pygame.display.set_caption(self.caption)

    def start(self):
        while self.running:
            self.tick()

    @timed
    def tick(self):
        self.clock.tick(self.fps)

        self.handle_events()

        self.update()

        self.display()

    @timed
    def handle_events(self):
        for event in pygame.event.get():
            if not self.parse_event(event):
                self.running = False

    def parse_event(self, event):
        return 1

    def update(self):
        self.screen.update()

    @timed
    def display(self):
        self.screen.display()
        pygame.display.flip()
