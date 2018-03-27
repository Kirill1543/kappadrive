from kappa.common.view.Viewable import Viewable
from kappa.core.font.Font import Font
from kappa.core.frame.Frame import Frame


class Text(Viewable):
    def __init__(self, text, font: Font, color):
        self.__texture = font.render(text, False, color)

    def view(self) -> Frame:
        return self.__texture
