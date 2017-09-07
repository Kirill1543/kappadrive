import random

from kappa.common.object.GameObject import GameObject
from kappa.core.Color import WHITE, RED
from kappa.core.geom import intersection_circle_with_circle, Circle, EPSILON
from kappa.core.geom.Point import Point
from kappa.core.primitives.Draw import Draw
from kappa.logger.Logger import Logger
from ..map.Box import Box
from ...Settings import Settings, NEAR_OBJECTS_MOVE
from ...core.frame.Frame import Frame


class BoxedMap:
    log = Logger(__name__).get()

    def __init__(self, width, height, levels=1):
        self.time = -1
        self.width = width
        self.height = height
        self.levels = levels
        self._boxes = []
        self._obj_draw_queue = None
        self._display_frame = None
        self._background_textures = None

    def __str__(self):
        out = ""
        for z, row1 in enumerate(self._boxes):
            for y, row2 in enumerate(row1):
                for x, val in enumerate(row2):
                    if val.object_list:
                        out += '({}:{}:{})-{}'.format(x, y, z, val.object_list)
        return out

    @property
    def box_width(self):
        return self.width // Settings.BOX_WIDTH

    @property
    def box_height(self):
        return self.height // Settings.BOX_HEIGHT

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
            pass

    def capture(self, x, y, w, h, l=0):
        self._obj_draw_queue = []
        self._display_frame = Frame((w, h))
        self._capture_background(x, y, w, h, l)
        self._draw_objects()
        self._obj_draw_queue = None

    def expand_boxes(self, input_boxes, delta):
        return (max(input_boxes[0][0] - delta, 0), max(input_boxes[0][1] - delta, 0)), (
            min(input_boxes[1][0] + delta, self.box_width - 1), min(input_boxes[1][1] + delta, self.box_height - 1))

    def get_near_obj_list(self, obj: GameObject):
        curr_box = int(obj.center.x) // Settings.BOX_WIDTH, int(obj.center.y) // Settings.BOX_HEIGHT
        lt, rb = self.expand_boxes((curr_box, curr_box), NEAR_OBJECTS_MOVE)
        objects = []
        for box_h in range(lt[1], rb[1] + 1):
            for box_w in range(lt[0], rb[0] + 1):
                for o in self._boxes[0][box_h][box_w].object_list:
                    if not o == obj:
                        objects.append(o)
        return objects

    def draw_lines(self, frame, obj, slicing):
        obj_list = self.get_near_obj_list(obj)
        for end_object in obj_list:
            BoxedMap.log.debug(
                "Drawing line between {} and {}".format(obj.center.coords, end_object.center.coords))
            Draw.line(frame, WHITE, obj.center - slicing, end_object.center - slicing, 1)
            if obj.intersect(end_object):
                Draw.line(frame, RED, obj.center - slicing, end_object.center - slicing, 1)
            Draw.circle(frame, WHITE, end_object.center - slicing, obj.shape.radius + end_object.shape.radius, 1)
            for end_object2 in obj_list:
                if not end_object == end_object2 and end_object.shape.is_circle and end_object2.shape.is_circle:
                    for c in intersection_circle_with_circle(
                            Circle(end_object.center, end_object.shape.radius + obj.shape.radius),
                            Circle(end_object2.center, end_object2.shape.radius + obj.shape.radius)):
                        BoxedMap.log.debug("Drawing circle for root={}".format(c))
                        Draw.circle(frame, RED, c - slicing, 5, 1)

    def try_move(self, obj: GameObject):
        if obj.is_movable and self.point_is_inside(obj.get_time_position()):
            near_objects = self.get_near_obj_list(obj)
            BoxedMap.log.debug("Trying to move {}. Found near object list:{}".format(obj, near_objects))
            vector = obj.move_vector
            if not vector.is_null():
                t = 1
                while t > EPSILON:
                    BoxedMap.log.debug("Default vector={}".format(vector))
                    t_1 = 1
                    found_object = None
                    for near_object in near_objects:
                        t_i = obj.move_time_to(near_object)
                        new_vector = t_i * vector
                        if abs(vector) > abs(new_vector):
                            vector = new_vector
                            t_1 = t_i
                            found_object = near_object
                            BoxedMap.log.debug("Vector updated with {} to {}".format(near_object, vector))
                    t -= t_1
                    obj.move_offset(vector)
                    if t < EPSILON:
                        break
                    intersections = []
                    for near_object in near_objects:
                        if not found_object == near_object and found_object.shape.is_circle and near_object.shape.is_circle:
                            for c in intersection_circle_with_circle(
                                    Circle(found_object.center, found_object.shape.radius + obj.shape.radius),
                                    Circle(near_object.center, near_object.shape.radius + obj.shape.radius)):
                                intersections += c
                    BoxedMap.log.debug("Found intersections:{}".format(intersections))
                    if not intersections:
                        t = 0
                    else:
                        pass

    def update(self):
        self.time += 1
        BoxedMap.log.debug("Time:{}".format(self.time))
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
