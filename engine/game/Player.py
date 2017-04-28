from engine.Settings import Settings
from engine.common.object.CircularObject import CircularObject
from engine.common.object.GameObject import GameObject
from engine.common.object.MovingObject import MovingObject


class Player(CircularObject, GameObject):
    def __init__(self, center, texture, r):
        CircularObject.__init__(self, center, texture, r)
        GameObject.__init__(self, MovingObject())
