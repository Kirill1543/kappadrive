from kappa.common.object.GameObject import GameObject
from kappa.common.object.Direction import Direction
from kappa.common.object.action.MoveAction import MoveAction


class StartMoveAction(MoveAction):
    @staticmethod
    def execute(obj: GameObject, direction):
        if direction in Direction.X:
            obj.x_move = direction
        elif direction in Direction.Y:
            obj.y_move = direction
        MoveAction.update_move(obj)
