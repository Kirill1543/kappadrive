from kappa.common.object.GameObject import GameObject
from kappa.core.geom.Point import Point
from kappa.logger.Logger import Logger
from ..map.Box import Box
from ...Settings import Settings
from ...core.frame.Frame import Frame
import random


class BoxedMap:
    log = Logger(__name__).get()

    def __init__(self, width, height, levels=1):
        self.width = width
        self.height = height
        self.levels = levels
        self._boxes = []
        self._obj_draw_queue = None
        self._display_frame = None
        self._background_textures = None

    def get_box_by_coords(self, coords):
        return self._boxes[coords[2]][coords[1] // Settings.BOX_HEIGHT][coords[0] // Settings.BOX_WIDTH]

    def get_box_by_point(self, point: Point):
        return self.get_box_by_coords((int(point.x), int(point.y), int(point.z)))

    def point_is_inside(self, point: Point):
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def set_random_background(self):
        w = self.width // Settings.BOX_WIDTH + (self.width % Settings.BOX_WIDTH > 0)
        h = self.height // Settings.BOX_HEIGHT + (self.height % Settings.BOX_HEIGHT > 0)
        self._boxes = []
        for l in range(0, self.levels):
            _map = []
            for i in range(0, h):
                _line = []
                for j in range(0, w):
                    _line.append(Box([[random.randint(0, 1) for i in range(0, Settings.BOX_TEXTURE_WIDTH)] for j in
                                      range(0, Settings.BOX_TEXTURE_HEIGHT)]))
                _map.append(_line)
            self._boxes.append(_map)

    def add_obj(self, obj):
        self.add_obj_to(obj, obj.center)

    def add_obj_to(self, obj, pos):
        obj.center = pos
        self.get_box_by_point(pos).add_obj(obj)

    def get_box(self, x, y, l=0):
        return self._boxes[l][y][x]

    def _capture_background(self, x, y, w, h, l=0):
        lt_box_id, rb_box_id = Box.get_id_by_rect(x, y, w, h)

        offset_h = max(y, 0) % Settings.BOX_HEIGHT
        pos_y = Settings.CAMERA_SCREEN_POSITION_Y - min(y, 0)
        for box_h in range(lt_box_id[1], rb_box_id[1] + 1):
            pos_x = Settings.CAMERA_SCREEN_POSITION_X - min(x, 0)
            offset_w = max(x, 0) % Settings.BOX_WIDTH

            for box_w in range(lt_box_id[0], rb_box_id[0] + 1):
                img_lt_corner = (offset_w, offset_h)
                img_size = (Settings.BOX_WIDTH - offset_w, Settings.BOX_HEIGHT - offset_h)
                curr_box = self._boxes[l][box_h][box_w]
                display_img = curr_box.build_background(self._background_textures)
                self._display_frame.display(display_img.subframe(img_lt_corner, img_size), (pos_x, pos_y))

                self._obj_draw_queue += curr_box.object_list

                pos_x += Settings.BOX_WIDTH - offset_w
                offset_w = 0

            pos_y += Settings.BOX_HEIGHT - offset_h
            offset_h = 0

    def _draw_objects(self):
        for obj in self._obj_draw_queue:
            obj.get_shape()

    def capture(self, x, y, w, h, l=0):
        self._obj_draw_queue = []
        self._display_frame = Frame((w, h))
        self._capture_background(x, y, w, h, l)
        self._draw_objects()
        self._obj_draw_queue = None

    def try_move(self, obj: GameObject):
        if self.point_is_inside(obj.center + obj.move_vector):
            obj.move()

    def update(self):
        move_list = []
        for row in self._boxes[0]:
            for box in row:
                for i, obj in enumerate(box.object_list):
                    move_list.append((obj, box, i))
        for obj, box, i in move_list:
            self.try_move(obj)
            if self.get_box_by_point(obj.center) != box:
                box.object_list.pop(i)
                self.add_obj(obj)

    @property
    def boxes(self):
        return self._boxes

    @boxes.setter
    def boxes(self, value):
        self._boxes = value

    def __str__(self):
        out = ""
        for z, row1 in enumerate(self._boxes):
            for y, row2 in enumerate(row1):
                for x, val in enumerate(row2):
                    if val.object_list:
                        out += '({}:{}:{})-{}'.format(x, y, z, val.object_list)
        return out
