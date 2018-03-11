from kappa.common.texture.Animation import Animation
from kappa.core.frame.Frame import Frame


class SimpleAnimation(Animation):
    def __init__(self, textures, update_ticks: int):
        Animation.__init__(self)
        self.__textures = textures
        self.__current_index = 0
        self.__update_tick = 0
        self.__update_max_tick = update_ticks

    def update(self):
        self.__update_tick += 1
        if self.__update_tick == self.__update_max_tick:
            self.__update_tick = 0
            self.__current_index += 1
            if self.__current_index == len(self.__textures):
                self.__current_index = 0

    def get(self) -> Frame:
        return self.__textures[self.__current_index]

    def reset(self):
        #  TODO: change to 0. Before adopt texture sources
        self.__update_tick = len(self.__textures) - 1
        self.__current_index = 0
