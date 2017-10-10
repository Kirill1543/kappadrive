import random

from ..map.Box import Box
from ..object.GameObject import GameObject
from ...Settings import NEAR_OBJECTS_MOVE, BOX_WIDTH, BOX_HEIGHT, BOX_TEXTURE_WIDTH, BOX_TEXTURE_HEIGHT
from ...core.Color import WHITE, RED, BLUE, GREEN
from ...core.geom import intersection_circle_with_circle, Circle, EPSILON
from ...core.geom.Point import Point
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

    def try_move(self, obj: GameObject):
        if obj.is_movable and self.point_is_inside(obj.get_time_position()):
            near_objects = self.get_near_obj_list(obj)
            BoxedMap.log.debug("Trying to move {}. Found near object list:{}".format(obj, near_objects))
            vector = obj.move_vector
            if not vector.is_null():
                t = 1.0
                while t > EPSILON:
                    BoxedMap.log.debug("Default vector={}".format(vector))
                    t_1 = 1.0
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
                    BoxedMap.log.debug("Moving forward with {} to {}; time = {}".format(vector, found_object, t_1))
                    obj.move_offset(vector)
                    if t < EPSILON:
                        break
                    intersections = []
                    tangent_points = []
                    closet_tangent_points = []
                    for near_object in near_objects:
                        if not found_object == near_object and found_object.shape.is_circle and near_object.shape.is_circle:
                            for c in intersection_circle_with_circle(
                                    Circle(found_object.center, found_object.shape.radius + obj.shape.radius),
                                    Circle(near_object.center, near_object.shape.radius + obj.shape.radius)):
                                intersections += [c]
                    points = Circle(found_object.center,
                                    found_object.shape.radius + obj.shape.radius).get_tangent_points(
                        obj.move_vector)
                    if abs(obj.center - points[0]) < abs(obj.center - points[1]):
                        closet_tangent_points += points[:1]
                    else:
                        closet_tangent_points += points[1:]
                    tangent_points += points

                    BoxedMap.log.debug("Found tangent points: {}".format(tangent_points))
                    BoxedMap.log.debug("Found closest tangent point: {}".format(closet_tangent_points))
                    BoxedMap.log.debug("Found intersections:{}".format(intersections))
                    if not intersections:
                        t = 0.0
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
