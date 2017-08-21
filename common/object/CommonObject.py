from kappa.core.geom.Point import Point
from ...Settings import Settings


class CommonObject(object):
    def __init__(self, center: Point, texture):
        self.center: Point = center
        self.texture = texture

    def center_in_box(self, i, j, l):
        return self.center.z == l and self.center.x / Settings.BOX_WIDTH == i and self.center.y / Settings.BOX_HEIGHT == j

    def center_on_coords(self, x, y):
        self.center.x = x
        self.center.y = y

    def center_on(self, c_obj):
        self.center_on_coords(c_obj.center.x, c_obj.center.y)
