from kappa.common.object.GameObject import GameObject
from kappa.common.object.action.Move import Move
from kappa.common.object.action.MoveAction import MoveAction


class StartMoveAction(MoveAction):
    @staticmethod
    def execute(obj: GameObject, direction):
        if direction in Move.X:
            obj.x_move = direction
        elif direction in Move.Y:
            obj.y_move = direction
        MoveAction.__update_move(obj)
