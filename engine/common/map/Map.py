from engine.common.map.Box import Box
from engine.Settings import Settings
import random


class Map(object):
    def __init__(self, width, height, levels=1):

        print "Map created"

        self.width = width
        self.height = height
        self.levels = levels
        self.boxes = []

    def get_box_by_coords(self, coords):
        return self.boxes[coords[2]][coords[1] / Settings.BOX_HEIGHT][coords[0] / Settings.BOX_WIDTH]

    def get_box_by_point(self, point):
        return self.get_box_by_coords([point.x, point.y, point.z])

    def set_random_background(self):

        print "New map random generation"

        w = self.width / Settings.BOX_WIDTH + (self.width % Settings.BOX_WIDTH > 0)
        h = self.height / Settings.BOX_HEIGHT + (self.height % Settings.BOX_HEIGHT > 0)
        print w, h
        self.boxes = []
        for l in xrange(0, self.levels):
            _map = []
            for i in xrange(0, h):
                _line = []
                for j in xrange(0, w):
                    _line.append(Box([[random.randint(0, 1) for i in xrange(0, Settings.BOX_TEXTURE_WIDTH)] for j in
                                      xrange(0, Settings.BOX_TEXTURE_HEIGHT)]))
                _map.append(_line)
            self.boxes.append(_map)

        print "Ended"

    def add_obj(self, obj):
        self.add_obj_to(obj, obj.center)

    def add_obj_to(self, obj, pos):
        obj.center = pos
        self.get_box_by_point(pos).object_list.append(obj)
