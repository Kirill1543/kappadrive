from ...core.Color import BLACK
from ...core.primitives.Draw import Draw
from ...Settings import BOX_HEIGHT, BOX_WIDTH, BOX_TEXTURE_HEIGHT, BOX_TEXTURE_WIDTH, BACKGROUND_TEXTURE_WIDTH, \
    BACKGROUND_TEXTURE_HEIGHT, DRAW_DEBUG
from ...core.frame.Frame import Frame


class Box:
    def __init__(self, background):
        self.__object_list = []
        self.__background = background

    def __str__(self):
        return str(self.__object_list)

    def __repr__(self):
        return self.__str__()

    def build_background(self):
        frame = Frame(size=(BOX_WIDTH, BOX_HEIGHT))
        for i in range(BOX_TEXTURE_HEIGHT):
            for j in range(BOX_TEXTURE_WIDTH):
                frame.display((self.__background[i][j]),
                              (j * BACKGROUND_TEXTURE_WIDTH, i * BACKGROUND_TEXTURE_HEIGHT))
        if DRAW_DEBUG:
            Draw.rect(frame, BLACK, (0, 0), (BOX_WIDTH, BOX_HEIGHT), 1)
        return frame

    def add_obj(self, obj):
        self.__object_list.append(obj)

    @staticmethod
    def get_id_by_coords(x, y, w=BOX_WIDTH, h=BOX_HEIGHT):
        return x // w, y // h

    @staticmethod
    def get_id_by_rect(x, y, w, h):
        return (Box.get_id_by_coords(max(int(x), 0), max(int(y), 0))), (
            Box.get_id_by_coords(min(int(x) + w, w) - 1, min(int(y) + h, h) - 1))

    @property
    def object_list(self):
        return self.__object_list

    @object_list.setter
    def object_list(self, value):
        self.__object_list = value
