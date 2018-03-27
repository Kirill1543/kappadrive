from ..camera.Camera import Camera
from ...core.frame.Frame import Frame


class Viewable:
    def view(self, **kwargs) -> Frame:
        pass

    def update(self):
        pass
