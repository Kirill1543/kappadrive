from math import sqrt

from kappa.common.object.GameObject import GameObject
from kappa.common.object.Direction import Direction
from kappa.core.geom import Vector
from . import init_property


class MoveAction:
    VECTORS = {
        Direction.NO: Vector(0, 0),
        Direction.LEFT: Vector(-1, 0),
        Direction.RIGHT: Vector(1, 0),
        Direction.UP: Vector(0, -1),
        Direction.DOWN: Vector(0, 1),
        Direction.UP_LEFT: Vector(-sqrt(2), -sqrt(2)),
        Direction.UP_RIGHT: Vector(sqrt(2), -sqrt(2)),
        Direction.DOWN_LEFT: Vector(-sqrt(2), sqrt(2)),
        Direction.DOWN_RIGHT: Vector(sqrt(2), sqrt(2)),
    }

    @staticmethod
    def init(obj: GameObject):
        init_property(obj, 'x_move', Direction.NO)
        init_property(obj, 'y_move', Direction.NO)
        init_property(obj, 'move_vector_normalized', MoveAction.VECTORS[Direction.NO])

    @staticmethod
    def update_move(obj: GameObject):
        obj.move_vector_normalized = MoveAction.VECTORS[obj.x_move + obj.y_move]
