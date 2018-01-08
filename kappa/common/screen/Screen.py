from ..view.View import View
from ...Settings import SCREEN_DEFAULT_WIDTH, SCREEN_DEFAULT_HEIGHT, BACKGROUND_DEFAULT_COLOR
from ...core.frame.Frame import Frame
from ...logger.Logger import Logger


class Screen:
    log = Logger(__name__).get()

    def __init__(self, w=SCREEN_DEFAULT_WIDTH, h=SCREEN_DEFAULT_HEIGHT):
        self.__screen = Frame.set_mode((w, h))
        self.background = Frame.empty((w, h))
        self.background.fill(BACKGROUND_DEFAULT_COLOR)

        self.__view_list = []

    def display(self):
        Screen.log.debug("Displaying background...")
        self.__screen.display(self.background, (0, 0))
        Screen.log.debug("Displaying view list...")
        for view in self.__view_list:
            Screen.log.debug("Displaying {}".format(view))
            self.__screen.display(view.display(), (view.x, view.y))

    def update(self):
        for view in self.__view_list:
            view.update()

    def add_view(self, view: View):
        self.__view_list.append(view)
