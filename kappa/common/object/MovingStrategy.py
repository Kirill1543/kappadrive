from ...core.geom.Vector import Vector


class MovingStrategy:
    def __init__(self):
        self.__speed = 0.0
        self.__move_vector_normalized: Vector = Vector(0.0, 0.0)

    def change_move(self, direction: str, k: int):
        pass

    def get_time_vector(self, t: float = 1) -> Vector:
        return Vector(0.0, 0.0)

    @property
    def is_movable(self) -> bool:
        return False

    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, value: float):
        self.__speed = value

    @property
    def move_vector(self):
        return self.__move_vector_normalized

    @move_vector.setter
    def move_vector(self, value: Vector):
        pass

    @property
    def move_vector_normalized(self):
        return self.__move_vector_normalized

    @move_vector_normalized.setter
    def move_vector_normalized(self, value: Vector):
        self.__move_vector_normalized = value
