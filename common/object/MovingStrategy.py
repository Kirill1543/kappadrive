from ...core.geom.Vector import Vector


class MovingStrategy:
    def __init__(self):
        pass

    def change_move(self, direction, k):
        pass

    def get_time_offset(self, t=1):
        return Vector(0.0, 0.0) * t

    @property
    def is_movable(self):
        return False
