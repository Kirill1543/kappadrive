from kappa.core.Color import BLACK


class Shape:
    def __init__(self, color=BLACK):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def get_shape(self):
        pass

    @property
    def width(self):
        return 0

    @property
    def height(self):
        return 0
