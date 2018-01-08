from ..view.View import View
from ...Settings import SCREEN_DEFAULT_WIDTH, SCREEN_DEFAULT_HEIGHT, BACKGROUND_DEFAULT_COLOR
from ...core.frame.Frame import Frame
from ...logger.Logger import Logger


class Screen(object):
    log = Logger(__name__).get()

    def __init__(self, w=SCREEN_DEFAULT_WIDTH, h=SCREEN_DEFAULT_HEIGHT):
        self.screen = Frame.set_mode((w, h))
        self.background = Frame.empty((w, h))
        self.background.fill(BACKGROUND_DEFAULT_COLOR)

        self.__view_list = []

    def display(self):
        Screen.log.debug("Displaying background...")
        self.screen.display(self.background, (0, 0))
        Screen.log.debug("Displaying view list...")
        for view in self.__view_list:
            Screen.log.debug("Displaying {}".format(view))
            self.screen.display(view.get(), (view.x, view.y))

    def update(self):
        for view in self.__view_list:
            view.update()

    def add_view(self, view: View):
        self.__view_list.append(view)
