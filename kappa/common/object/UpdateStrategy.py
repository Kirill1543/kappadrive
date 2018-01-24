from ...core.frame.Frame import Frame
from ...core.geom.Vector import Vector


class UpdateStrategy:
    def __init__(self, textures=None, update_ticks=9):
        self.__speed = 0.0
        self.__move_vector_normalized: Vector = Vector(0.0, 0.0, 0.0)
        self.__texture_list = None
        self.textures = textures
        self.__current_index = 0
        self.__update_tick = 0
        self.__update_max_tick = update_ticks

    def start_move(self, direction):
        pass

    def stop_move(self, direction):
        pass

    def get_time_vector(self, t: float = 1) -> Vector:
        return Vector(0.0, 0.0, 0.0)

    def update(self):
        self.__update_tick += 1
        if self.__update_tick == self.__update_max_tick:
            self.__update_tick = 0
            self.__current_index += 1
            if self.__current_index == len(self.__texture_list):
                self.__current_index = 0

    def reset(self):
        self.__update_tick = len(self.__texture_list) - 1
        self.__current_index = 0

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

    @property
    def texture(self) -> Frame:
        return self.__texture_list[self.__current_index]

    @property
    def textures(self):
        return self.__texture_list

    @textures.setter
    def textures(self, value):
        if isinstance(value, Frame):
            self.__texture_list = [value]
        else:
            self.__texture_list = value

    @property
    def update_ticks(self):
        return self.__update_max_tick

    @update_ticks.setter
    def update_ticks(self, value):
        self.__update_max_tick = value
