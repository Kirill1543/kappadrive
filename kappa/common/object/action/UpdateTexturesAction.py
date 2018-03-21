from kappa.common.object.GameObject import GameObject


class UpdateTexturesAction:
    @staticmethod
    def execute(obj: GameObject):
        obj.textures = obj.texture_controller.get_textures(obj)
