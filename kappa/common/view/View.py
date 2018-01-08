from . import Viewable
from ..camera.Camera import Camera
from ...core.frame import Frame


class View:
    def __init__(self, viewable: Viewable, coords=(0, 0), camera: Camera = Camera()):
        self.__x = coords[0]
        self.__y = coords[1]
        self.__viewable: Viewable = viewable
        self.__camera: Camera = camera

    def __str__(self):
        return "View<{}:{}:({},{})>".format(self.__viewable, self.__camera, self.__x, self.__y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def camera(self):
        return self.__camera

    @camera.setter
    def camera(self, value: Camera):
        self.__camera = value

    def display(self) -> Frame:
        return self.__viewable.view(self.__camera)

    def update(self):
        self.__viewable.update()
