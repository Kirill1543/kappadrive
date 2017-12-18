from ...core.geom.Point import Point


class CommonObject(object):
    def __init__(self, center: Point, texture):
        self.center = center
        self.texture = texture

    def center_on(self, c_obj: __name__):
        self.move_to(c_obj.center)

    def move_to(self, point: Point):
        self.center = point
