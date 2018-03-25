from kappa.common.object.Direction import Direction
from kappa.common.object.GameObject import GameObject
from kappa.common.object.State import State
from kappa.common.object.action.Action import Action
from kappa.common.object.action.ActionStatus import ActionStatus
from kappa.common.object.action.ActionType import ActionType
from kappa.common.object.action.UpdateMoveAction import UpdateMoveAction


class StopMoveAction(Action):
    def execute(self, obj: GameObject, **kwargs):
        if 'direction' in kwargs.keys():
            direction = kwargs['direction']
            if direction == obj.x_move:
                obj.x_move = Direction.NO
            elif direction == obj.y_move:
                obj.y_move = Direction.NO
            else:
                return ActionStatus.SKIP
        else:
            obj.x_move = Direction.NO
            obj.y_move = Direction.NO
        if obj.x_move + obj.y_move == Direction.NO:
            obj.state = State.STAND
        UpdateMoveAction().execute(obj)
        return ActionStatus.SUCCESS

    @property
    def name(self):
        return ActionType.STOP_MOVE
