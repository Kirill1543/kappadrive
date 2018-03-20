from kappa.common.object.GameObject import GameObject
from kappa.common.object.Direction import Direction
from kappa.common.object.action.MoveAction import MoveAction


class StopMoveAction(MoveAction):
    @staticmethod
    def execute(obj: GameObject, direction):
        if direction == obj.x_move:
            obj.x_move = Direction.NO
        elif direction == obj.y_move:
            obj.y_move = Direction.NO
        MoveAction.update_move(obj)
