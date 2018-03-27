from kappa.common.view.Viewable import Viewable
from kappa.core.frame.Frame import Frame


class VariableText(Viewable):
    def __init__(self, text, font, color, *args):
        self.__text = text
        self.__font = font
        self.__color = color
        self.__vars = args

    def view(self) -> Frame:
        return self.__font.render(self.__text.format(*[var() for var in self.__vars]), False, self.__color)
