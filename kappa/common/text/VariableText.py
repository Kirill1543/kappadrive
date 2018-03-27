from kappa.common.view.Viewable import Viewable
from kappa.core.frame.Frame import Frame


class VariableText(Viewable):
    def __init__(self, text_supplier, font, color):
        self.__text_supplier = text_supplier
        self.__font = font
        self.__color = color

    def view(self) -> Frame:
        return self.__font.render(self.__text_supplier(), False, self.__color)
