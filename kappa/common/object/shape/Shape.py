from kappa.core.Color import BLACK


class Shape:
    def __init__(self, color=BLACK):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def shape(self):
        return None

    @property
    def width(self):
        return 0

    @property
    def height(self):
        return 0

    @property
    def radius(self):
        return 0

    @property
    def is_circle(self) -> bool:
        return False

    @property
    def is_rect(self) -> bool:
        return False
