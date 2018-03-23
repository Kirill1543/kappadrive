from kappa.common.object.Direction import Direction
from kappa.common.object.GameObject import GameObject
from kappa.common.object.State import State
from kappa.common.object.action.Action import Action
from kappa.common.object.action.ActionStatus import ActionStatus
from kappa.common.object.action.ActionType import ActionType
from kappa.common.object.action.UpdateMoveAction import UpdateMoveAction


class StartMoveAction(Action):
    def execute(self, obj: GameObject, **kwargs):
        direction = kwargs['direction']
        if direction in Direction.X and obj.x_move != direction:
            obj.x_move = direction
        elif direction in Direction.Y and obj.y_move != direction:
            obj.y_move = direction
        else:
            return ActionStatus.SKIP
        obj.state = State.MOVE
        UpdateMoveAction().execute(obj)
        return ActionStatus.SUCCESS

    @property
    def name(self):
        return ActionType.START_MOVE
