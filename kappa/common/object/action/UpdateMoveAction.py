from math import sqrt

from kappa.common.object.Direction import Direction
from kappa.common.object.GameObject import GameObject
from kappa.common.object.action.Action import Action
from kappa.common.object.action.ActionStatus import ActionStatus
from kappa.common.object.action.ActionType import ActionType
from kappa.core.geom import Vector


class UpdateMoveAction(Action):
    SQRT2_HALF = sqrt(2) / 2

    VECTORS = {
        Direction.NO: Vector(0, 0, 0),
        Direction.LEFT: Vector(-1, 0, 0),
        Direction.RIGHT: Vector(1, 0, 0),
        Direction.UP: Vector(0, -1, 0),
        Direction.DOWN: Vector(0, 1, 0),
        Direction.UP_LEFT: Vector(-SQRT2_HALF, -SQRT2_HALF, 0),
        Direction.UP_RIGHT: Vector(SQRT2_HALF, -SQRT2_HALF, 0),
        Direction.DOWN_LEFT: Vector(-SQRT2_HALF, SQRT2_HALF, 0),
        Direction.DOWN_RIGHT: Vector(SQRT2_HALF, SQRT2_HALF, 0),
    }

    def execute(self, obj: GameObject):
        direction = obj.x_move + obj.y_move
        obj.move_vector_normalized = UpdateMoveAction.VECTORS[direction]
        if direction != Direction.NO:
            obj.direction = direction
        return ActionStatus.SUCCESS

    @property
    def name(self):
        return ActionType.UPDATE_MOVE
