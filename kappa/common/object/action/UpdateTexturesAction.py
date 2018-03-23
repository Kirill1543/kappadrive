from kappa.common.object.GameObject import GameObject
from kappa.common.object.action.Action import Action
from kappa.common.object.action.ActionStatus import ActionStatus
from kappa.common.object.action.ActionType import ActionType


class UpdateTexturesAction(Action):
    def execute(self, obj: GameObject):
        obj.textures = obj.texture_controller.get_textures(obj)
        return ActionStatus.SUCCESS

    @property
    def name(self):
        return ActionType.UPDATE_TEXTURE
