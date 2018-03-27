from . import Viewable
from ..camera.Camera import Camera
from ...core.frame import Frame


class View:
    def __init__(self, viewable: Viewable, camera: Camera = None):
        self.__viewable: Viewable = viewable
        self.__camera: Camera = camera

    def __str__(self):
        return "View<{}:{}>".format(self.__viewable, self.__camera)

    @property
    def camera(self):
        return self.__camera

    @camera.setter
    def camera(self, value: Camera):
        self.__camera = value

    def display(self) -> Frame:
        if self.__camera:
            return self.__viewable.view(self.__camera)
        else:
            return self.__viewable.view()

    def update(self):
        self.__viewable.update()
