from ...common.object.MovingStrategy import MovingStrategy
from ...core.geom.Vector import Vector
from ...logger.Logger import Logger


class SimpleMovingStrategy(MovingStrategy):
    log = Logger(__name__).get()

    def __init__(self, vector: Vector = Vector(0.0, 0.0, 0.0), speed: float = 0.0):
        super().__init__()
        self.speed = speed
        self.move_vector = vector

    def change_move(self, direction: str, k: int):
        SimpleMovingStrategy.log.debug("Switching moving vector with value={}".format(k))
        if direction == 'UP':
            self.move_vector_normalized[1] -= k
        elif direction == 'DOWN':
            self.move_vector_normalized[1] += k
        elif direction == 'LEFT':
            self.move_vector_normalized[0] -= k
        elif direction == 'RIGHT':
            self.move_vector_normalized[0] += k
        SimpleMovingStrategy.log.debug("Move vector is now = {}".format(self.move_vector))

    def get_time_vector(self, t: float = 1) -> Vector:
        return self.move_vector * t

    @property
    def is_movable(self):
        return True

    @property
    def move_vector(self):
        return self.move_vector_normalized * self.speed

    @move_vector.setter
    def move_vector(self, value: Vector):
        self.move_vector_normalized = value.normalize()
        self.speed = abs(value)
