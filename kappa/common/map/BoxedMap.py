import random

from ..map.Box import Box
from ..object.GameObject import GameObject
from ...Settings import NEAR_OBJECTS_MOVE, BOX_WIDTH, BOX_HEIGHT, BOX_TEXTURE_WIDTH, BOX_TEXTURE_HEIGHT
from ...core.Color import WHITE, RED, BLUE, GREEN
from ...core.geom import intersection_circle_with_circle, Circle, EPSILON, Point, Angle
from ...core.primitives.Draw import Draw
from ...logger.Logger import Logger


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
        return self.width // BOX_WIDTH

    @property
    def box_height(self):
        return self.height // BOX_HEIGHT

    def get_box_by_coords(self, coords):
        return self._boxes[coords[2]][coords[1] // BOX_HEIGHT][coords[0] // BOX_WIDTH]

    def get_box_by_point(self, point: Point):
        return self.get_box_by_coords((int(point.x), int(point.y), int(point.z)))

    def point_is_inside(self, point: Point):
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def set_random_background(self):
        w = self.width // BOX_WIDTH + (self.width % BOX_WIDTH > 0)
        h = self.height // BOX_HEIGHT + (self.height % BOX_HEIGHT > 0)
        self._boxes = []
        for l in range(0, self.levels):
            _map = []
            for i in range(0, h):
                _line = []
                for j in range(0, w):
                    _line.append(Box([[random.randint(0, 1) for i in range(0, BOX_TEXTURE_WIDTH)] for j in
                                      range(0, BOX_TEXTURE_HEIGHT)]))
                _map.append(_line)
            self._boxes.append(_map)

    def add_obj(self, obj):
        self.add_obj_to(obj, obj.center)

    def add_obj_to(self, obj, pos):
        obj.center = pos
        self.get_box_by_point(pos).add_obj(obj)

    def expand_boxes(self, input_boxes, delta):
        return (max(input_boxes[0][0] - delta, 0), max(input_boxes[0][1] - delta, 0)), (
            min(input_boxes[1][0] + delta, self.box_width - 1), min(input_boxes[1][1] + delta, self.box_height - 1))

    def get_near_obj_list(self, obj: GameObject):
        curr_box = int(obj.center.x) // BOX_WIDTH, int(obj.center.y) // BOX_HEIGHT
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
            points = Circle(end_object.center, end_object.shape.radius + obj.shape.radius).get_tangent_points(
                obj.move_vector)
            points.sort(key=lambda x: abs(x - obj.center))
            BoxedMap.log.debug("Drawing circle for closest tangent point={}".format(points[0]))
            Draw.circle(frame, BLUE, points[0] - slicing, 5, 1)
            BoxedMap.log.debug("Drawing circle for farest tangent point={}".format(points[1]))
            Draw.circle(frame, GREEN, points[1] - slicing, 5, 1)

    def __find_closest_object(self, obj: GameObject) -> (bool, float):
        BoxedMap.log.debug("Finding closest object for {}. Minimum time is set as 1.0.".format(obj))
        is_stuck_point: bool = False
        found: bool = False
        minimum_time: float = 1.0
        near_objects = self.get_near_obj_list(obj)

        for near_object in near_objects:
            time_i: float = obj.move_time_to(near_object)
            if abs(time_i - minimum_time) <= EPSILON:
                if found:
                    BoxedMap.log.debug("Found duplicate. Setting flag is_stuck_point = True.")
                    is_stuck_point = True

            if time_i < minimum_time - EPSILON:
                BoxedMap.log.debug(
                    "Found closest object, setting minimum time as {}, setting is_stuck_point=false".format(time_i))
                minimum_time = time_i
                found = True
                is_stuck_point = False

        if minimum_time < EPSILON:
            BoxedMap.log.debug("Minimum time={} is very small, correcting it to 0.".format(minimum_time))
            minimum_time = 0.0

        return is_stuck_point, minimum_time

    def __try_move(self, obj: GameObject):
        if not obj.is_movable:
            BoxedMap.log.debug("Skipping moving iteration for {}: Not movable".format(obj))
            return

        if not self.point_is_inside(obj.get_time_position()):
            BoxedMap.log.debug("Skipping moving iteration for {}: Destination point outside map borders".format(obj))
            return

        if obj.move_vector.is_null():
            BoxedMap.log.debug("Skipping moving iteration for {}: Moving vector is null".format(obj))
            return

        BoxedMap.log.debug("Starting moving iteration for {}.".format(obj))
        is_stuck, minimum_time = self.__find_closest_object(obj)

        if is_stuck:
            BoxedMap.log.debug("Having stuck point in {} time. Moving and ending iteration".format(minimum_time))
            obj.move(minimum_time)
            return

        obj.move(minimum_time)

    def update(self):
        self.time += 1
        BoxedMap.log.debug("Time:{}".format(self.time))
        move_list = []
        for row in self._boxes[0]:
            for box in row:
                for i, obj in enumerate(box.object_list):
                    move_list.append((obj, box, i))
        for obj, box, i in move_list:
            self.__try_move(obj)
            if self.get_box_by_point(obj.center) != box:
                box.object_list.pop(i)
                self.add_obj(obj)

    @property
    def boxes(self):
        return self._boxes

    @boxes.setter
    def boxes(self, value):
        self._boxes = value
