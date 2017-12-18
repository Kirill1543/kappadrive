from ...core.geom.Point import Point


class CommonObject(object):
    def __init__(self, center: Point, texture):
        self.center = center
        self.texture = texture

    def __str__(self) -> str:
        return "{}:{}".format(self.__class__.__name__, self.center.coords)

    def __repr__(self):
        return self.__str__()

    def center_on(self, c_obj: __name__):
        self.move_to(c_obj.center)

    def move_to(self, point: Point):
        self.center = point
