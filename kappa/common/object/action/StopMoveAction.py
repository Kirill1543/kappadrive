from kappa.common.object.GameObject import GameObject
from kappa.common.object.action.Move import Move
from kappa.common.object.action.MoveAction import MoveAction


class StopMoveAction(MoveAction):
    @staticmethod
    def execute(obj: GameObject, direction):
        if direction == obj.x_move:
            obj.x_move = Move.NO
        elif direction == obj.y_move:
            obj.y_move = Move.NO
        MoveAction.update_move(obj)
