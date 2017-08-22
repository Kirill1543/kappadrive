from kappa.core.Color import BLACK
from kappa.core.primitives.Draw import Draw
from ...Settings import Settings
from ...core.frame.Frame import Frame


class Box:
    def __init__(self, background):
        self._object_list = []
        self._background = background

    def build_background(self, textures):
        frame = Frame(size=(Settings.BOX_WIDTH, Settings.BOX_HEIGHT))
        for i in range(Settings.BOX_TEXTURE_HEIGHT):
            for j in range(Settings.BOX_TEXTURE_WIDTH):
                frame.display(textures[self._background[i][j]],
                              (j * Settings.BACKGROUND_TEXTURE_WIDTH, i * Settings.BACKGROUND_TEXTURE_HEIGHT))
        Draw.rect(frame, BLACK, (0, 0), (Settings.BOX_WIDTH, Settings.BOX_HEIGHT), 1)
        return frame

    def add_obj(self, obj):
        self._object_list.append(obj)

    @staticmethod
    def get_id_by_coords(x, y, w=Settings.BOX_WIDTH, h=Settings.BOX_HEIGHT):
        return x // w, y // h

    @staticmethod
    def get_id_by_rect(x, y, w, h):
        return (Box.get_id_by_coords(max(int(x), 0), max(int(y), 0))), (
            Box.get_id_by_coords(min(int(x) + w, w) - 1, min(int(y) + h, h) - 1))

    @property
    def object_list(self):
        return self._object_list

    @object_list.setter
    def object_list(self, value):
        self._object_list = value

    def __str__(self):
        return str(self.object_list)
