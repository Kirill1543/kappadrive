import random

import pygame

from ..camera import Camera
from ..map.Box import Box
from ..object.GameObject import GameObject
from ..view.Viewable import Viewable
from ...Settings import NEAR_OBJECTS_MOVE, BOX_WIDTH, BOX_HEIGHT, BOX_TEXTURE_WIDTH, BOX_TEXTURE_HEIGHT, \
    NEAR_OBJECTS_DRAW, DRAW_DEBUG, BACKGROUND_TEXTURE_WIDTH, BACKGROUND_TEXTURE_HEIGHT, BACKGROUND_TEXTURE_SOURCE_WIDTH, \
    BACKGROUND_TEXTURE_SOURCE_HEIGHT
from ...core.Color import WHITE, RED, BLUE, GREEN
from ...core.frame.Frame import Frame
from ...core.geom import intersection_circle_with_circle, Circle, EPSILON, Point
from ...core.primitives.Draw import Draw
from ...logger.Logger import Logger


class BoxedMap(Viewable):
    log = Logger(__name__).get()

    def __init__(self, width, height, levels=1):
        self.time = -1
        self.width = width
        self.height = height
        self.levels = levels
        self.__boxes = []
        self.__display_obj_queue = None
        self.__display_frame = None
        self.__background_textures = []

    def __str__(self):
        out = ""
        for z, row1 in enumerate(self.__boxes):
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

    @staticmethod
    def get_box_id_by_coords(x, y):
        return x // BOX_WIDTH, y // BOX_HEIGHT

    def get_box_by_coords(self, coords):
        return self.__boxes[coords[2]][coords[1] // BOX_HEIGHT][coords[0] // BOX_WIDTH]

    def get_box_by_point(self, point: Point):
        return self.get_box_by_coords((int(point.x), int(point.y), int(point.z)))

    def get_boxes_by_camera(self, camera: Camera):
        return (self.get_box_id_by_coords(max(int(camera.x), 0), max(int(camera.y), 0))), (
            self.get_box_id_by_coords(min(int(camera.x) + camera.width, self.width) - 1,
                                      min(int(camera.y) + camera.height, self.height) - 1))

    def point_is_inside(self, point: Point):
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def set_random_background(self):
        w = self.width // BOX_WIDTH + (self.width % BOX_WIDTH > 0)
        h = self.height // BOX_HEIGHT + (self.height % BOX_HEIGHT > 0)
        self.__boxes = []
        for l in range(0, self.levels):
            _map = []
            for i in range(0, h):
                _line = []
                for j in range(0, w):
                    _line.append(Box([[random.randint(0, 1) for i in range(0, BOX_TEXTURE_WIDTH)] for j in
                                      range(0, BOX_TEXTURE_HEIGHT)]))
                _map.append(_line)
            self.__boxes.append(_map)

    def add_obj(self, obj):
        self.add_obj_to(obj, obj.center)

    def add_obj_to(self, obj, pos):
        obj.center = pos
        self.get_box_by_point(pos).add_obj(obj)

    def __display_background(self, camera: Camera, frame: Frame):
        lt_box_id, rb_box_id = self.get_boxes_by_camera(camera)
        BoxedMap.log.debug("Selected draw boxes:{}-{}".format(lt_box_id, rb_box_id))
        offset_h = max(int(camera.y), 0) % BOX_HEIGHT
        pos_y = -min(camera.y, 0)
        for box_h in range(lt_box_id[1], rb_box_id[1] + 1):
            offset_w = max(int(camera.x), 0) % BOX_WIDTH
            pos_x = -min(camera.x, 0)

            for box_w in range(lt_box_id[0], rb_box_id[0] + 1):
                img_lt_corner = (offset_w, offset_h)
                img_size = (BOX_WIDTH - offset_w, BOX_HEIGHT - offset_h)
                curr_box = self.boxes[int(camera.center.z)][box_h][box_w]
                img_to_blit = curr_box.build_background(self.__background_textures)
                frame.display(img_to_blit.subframe(*img_lt_corner, *img_size), (pos_x, pos_y))

                pos_x += BOX_WIDTH - offset_w
                offset_w = 0

            pos_y += BOX_HEIGHT - offset_h
            offset_h = 0

        for box_h in range(min(lt_box_id[1] - NEAR_OBJECTS_DRAW, 0),
                           max(rb_box_id[1] + NEAR_OBJECTS_DRAW, self.box_height)):
            for box_w in range(min(lt_box_id[0] - NEAR_OBJECTS_DRAW, 0),
                               max(rb_box_id[0] + NEAR_OBJECTS_DRAW, self.box_width)):
                self.__display_obj_queue += self.boxes[int(camera.center.z)][box_h][box_w].object_list

    def __display_objects(self, camera: Camera, frame: Frame):
        BoxedMap.log.debug("BoxedMap objects list:{}".format(self))
        for obj in self.__display_obj_queue:
            slicing = camera.topleft - Point(0, 0, 0)
            obj.draw_shape_on(frame, obj.center - slicing)
            if obj.is_movable and DRAW_DEBUG:
                self.__draw_lines(frame, obj, slicing)

    def view(self, camera: Camera) -> Frame:
        BoxedMap.log.debug("Camera LeftTop Position:{}".format((camera.x, camera.y)))
        frame = Frame((camera.width, camera.height))

        self.__display_obj_queue = []

        self.__display_background(camera, frame)
        self.__display_objects(camera, frame)

        self.__display_obj_queue = None

        return frame

    def expand_boxes(self, input_boxes, delta):
        return (max(input_boxes[0][0] - delta, 0), max(input_boxes[0][1] - delta, 0)), (
            min(input_boxes[1][0] + delta, self.box_width - 1), min(input_boxes[1][1] + delta, self.box_height - 1))

    def get_near_obj_list(self, obj: GameObject):
        curr_box = int(obj.center.x) // BOX_WIDTH, int(obj.center.y) // BOX_HEIGHT
        lt, rb = self.expand_boxes((curr_box, curr_box), NEAR_OBJECTS_MOVE)
        objects = []
        for box_h in range(lt[1], rb[1] + 1):
            for box_w in range(lt[0], rb[0] + 1):
                for o in self.__boxes[0][box_h][box_w].object_list:
                    if not o == obj:
                        objects.append(o)
        return objects

    def __draw_lines(self, frame, obj, slicing):
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
        for row in self.__boxes[0]:
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
        return self.__boxes

    @boxes.setter
    def boxes(self, value):
        self.__boxes = value
