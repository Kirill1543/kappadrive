from math import sqrt


class Coordinates:
    def __init__(self, *args):
        self.__coords = list(args)

    def __str__(self) -> str:
        return "{}:{}".format(self.__class__.__name__, self.__coords)

    def __repr__(self):
        return self.__str__()

    @property
    def x(self):
        return self.__coords[0]

    @x.setter
    def x(self, value):
        self.__coords[0] = value

    @property
    def y(self):
        return self.__coords[1]

    @y.setter
    def y(self, value):
        self.__coords[1] = value

    @property
    def z(self):
        return self.__coords[2]

    @z.setter
    def z(self, value):
        self.__coords[2] = value

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, value):
        self.__coords = value

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def __len__(self):
        return len(self.__coords)

    def __mul__(self, other):
        if isinstance(other, float):
            return Coordinates(*list(x * other for x in self.coords))
        if isinstance(other, Coordinates):
            return sum(x * y for x, y in zip(self.coords, other.coords))
        raise NotImplementedError("Not supported to mul non-(Coordinates or float) and Coordinates")

    def __abs__(self):
        return sqrt(self * self)
