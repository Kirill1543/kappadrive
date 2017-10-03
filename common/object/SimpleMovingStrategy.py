from ...common.object.MovingStrategy import MovingStrategy
from ...core.geom.Vector import Vector
from ...logger.Logger import Logger


class SimpleMovingStrategy(MovingStrategy):
    log = Logger(__name__).get()

    def __init__(self, vector: Vector = Vector(0.0, 0.0, 0.0), speed=3.0):
        super().__init__()
        self.speed: float = speed
        self._move_vector: Vector = vector

    def change_move(self, direction, k):
        if direction == u'UP':
            self._move_vector[1] -= k
        elif direction == u'DOWN':
            self._move_vector[1] += k
        elif direction == u'LEFT':
            self._move_vector[0] -= k
        elif direction == u'RIGHT':
            self._move_vector[0] += k

    def get_time_offset(self, t=1):
        return self._move_vector.normalize() * self.speed * t

    @property
    def move_vector(self, t=1):
        return self._move_vector.normalize() * self.speed * t

    @move_vector.setter
    def move_vector(self, value: Vector):
        self._move_vector = value

    @property
    def is_movable(self):
        return True
