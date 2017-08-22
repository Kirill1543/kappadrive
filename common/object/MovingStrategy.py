from kappa.core.geom.Vector import Vector


class MovingStrategy:
    def __init__(self):
        pass

    def change_move(self, direction, k):
        pass

    def move(self, center):
        pass

    @property
    def move_vector(self):
        return Vector(0.0, 0.0)

    @move_vector.setter
    def move_vector(self, value: Vector):
        pass

    @property
    def is_movable(self):
        return False
