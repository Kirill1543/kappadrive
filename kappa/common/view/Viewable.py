from ..camera.Camera import Camera
from ...core.frame.Frame import Frame


class Viewable:
    def view(self, camera: Camera) -> Frame:
        return Frame.empty((camera.width, camera.height))

    def update(self):
        pass
