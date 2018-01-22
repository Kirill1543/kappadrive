from ...Settings import DRAW_DEBUG
from ...core.Color import BLACK
from ...core.frame.Frame import Frame
from ...core.primitives.Draw import Draw


class Box:
    def __init__(self, size, background):
        self.size = size
        self.__object_list = []
        self.__background = background

    def __str__(self):
        return str(self.__object_list)

    def __repr__(self):
        return self.__str__()

    def build_background(self):
        frame = Frame(self.size)
        background_height = len(self.__background)
        background_width = len(self.__background[0])
        for i in range(background_height):
            for j in range(background_width):
                frame.display((self.__background[j][i]),
                              (j * self.size[0] // background_width, i * self.size[1] // background_height))
        if DRAW_DEBUG:
            Draw.rect(frame, BLACK, (0, 0), self.size, 1)
        return frame

    def add_obj(self, obj):
        self.__object_list.append(obj)

    @property
    def object_list(self):
        return self.__object_list

    @object_list.setter
    def object_list(self, value):
        self.__object_list = value
