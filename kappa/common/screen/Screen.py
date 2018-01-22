from ..view.View import View
from ...core.frame.Frame import Frame
from ...logger.Logger import Logger


class Screen:
    log = Logger(__name__).get()
    BACKGROUND_DEFAULT_COLOR = (0, 0, 0)

    def __init__(self, size):
        self.__screen = Frame.set_mode(size)
        self.background = Frame.empty(size)
        self.background.fill(Screen.BACKGROUND_DEFAULT_COLOR)

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
