class Coordinates:
    def __init__(self, *args):
        self._coords = list(args)

    @property
    def x(self):
        return self._coords[0]

    @x.setter
    def x(self, value):
        self._coords[0] = value

    @property
    def y(self):
        return self._coords[1]

    @y.setter
    def y(self, value):
        self._coords[1] = value

    @property
    def z(self):
        return self._coords[2]

    @z.setter
    def z(self, value):
        self._coords[2] = value

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, value):
        self._coords = value

    def __getitem__(self, item):
        return self._coords[item]

    def __len__(self):
        return len(self._coords)
