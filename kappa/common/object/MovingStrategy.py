from ...core.geom.Vector import Vector


class MovingStrategy:
    def __init__(self):
        self._speed = 0.0

    def change_move(self, direction, k):
        pass

    def get_time_offset(self, t=1):
        return Vector(0.0, 0.0) * t

    @property
    def is_movable(self) -> bool:
        return False

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, value: float):
        self._speed = value
