from engine.Settings import Settings
from engine.common.object.CircularObject import CircularObject
from engine.common.object.ObjectBehavior import ObjectBehavior
from engine.common.object.MovingObject import MovingObject


class Player(CircularObject, ObjectBehavior):
    def __init__(self, center, texture, r):
        CircularObject.__init__(self, center, texture, r)
        ObjectBehavior.__init__(self, MovingObject())
