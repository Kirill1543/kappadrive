from kappa.common.object.GameObject import GameObject
from kappa.common.object.action.ActionStatus import ActionStatus


class UpdateTexturesAction:
    @staticmethod
    def execute(obj: GameObject):
        obj.textures = obj.texture_controller.get_textures(obj)
        return ActionStatus.SUCCESS
