import timeit

import pygame
from pygame.time import Clock

from ..common.screen.Screen import Screen
from ..logger.Logger import Logger


def timed(method):
    def _timed(*args, **kwargs):
        start_time = timeit.default_timer()
        name = method.__name__[2:]
        Instance.log.debug("Started {} iteration".format(name))
        method(*args, **kwargs)
        Instance.log.debug(
            "Finished {} iteration. Time={}ms".format(name, (timeit.default_timer() - start_time) * 1000))

    return _timed


class Instance:
    log = Logger(__name__).get()

    def __init__(self, caption: str = 'kappa game'):
        pygame.init()
        self.caption: str = caption
        self.clock: Clock = None
        self.screen: Screen = None
        self.running = True
        self.max_fps = 0

    def init(self):
        self.clock = Clock()
        pygame.display.set_caption(self.caption)
        self.screen.init()

    def start(self):
        while self.running:
            self.__tick()

    @timed
    def __tick(self):
        self.clock.tick(self.max_fps)

        self.__handle_events()

        self.__update()

        self.__display()

    @timed
    def __handle_events(self):
        for event in pygame.event.get():
            Instance.log.debug("Caught Event = {}".format(event))
            if not self.parse_event(event):
                self.running = False

    def parse_event(self, event):
        return 1

    @timed
    def __update(self):
        self.update()

    def update(self):
        self.screen.update()

    @timed
    def __display(self):
        self.screen.display()
        pygame.display.flip()
        Instance.log.debug("Current FPS : {}".format(self.fps))

    @property
    def fps(self):
        return self.clock.get_fps()
