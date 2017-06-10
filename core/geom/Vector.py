class Vector:
    def __init__(self, coords):
        self._coords = coords

    @property
    def dimension(self):
        return len(self._coords)

    def __len__(self):
        return len(self._coords)

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

