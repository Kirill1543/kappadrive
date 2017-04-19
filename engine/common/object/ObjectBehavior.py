class ObjectBehavior(object):
    def __init__(self, moving_style):
        self._m = moving_style

    def update(self):
        self.move()

    def move(self):
        self._m.move()
