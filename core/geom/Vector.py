class Vector:
    def __init__(self, coords):
        self._coords = coords

    @property
    def dimension(self):
        return len(self._coords)
