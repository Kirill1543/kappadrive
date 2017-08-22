from kappa.common.object.MovingStrategy import MovingStrategy
from kappa.core.geom.Vector import Vector
from kappa.logger.Logger import Logger


class SimpleMovingStrategy(MovingStrategy):
    log = Logger(__name__).get()

    def __init__(self, vector: Vector = Vector(0.0, 0.0), speed=3.0):
        super().__init__()
        self.speed = speed
        self._move_vector: Vector = vector

    def change_move(self, direction, k):
        k = k * self.speed
        if direction == u'UP':
            self._move_vector[1] -= k
        elif direction == u'DOWN':
            self._move_vector[1] += k
        elif direction == u'LEFT':
            self._move_vector[0] -= k
        elif direction == u'RIGHT':
            self._move_vector[0] += k

    def move(self, center):
        center.x += self._move_vector[0]
        center.y += self._move_vector[1]

    @property
    def move_vector(self):
        return self._move_vector

    @move_vector.setter
    def move_vector(self, value: Vector):
        self._move_vector = value

    @property
    def is_movable(self):
        return True
