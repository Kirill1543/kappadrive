from kappa.common.object.GameObject import GameObject
from kappa.common.object.action.Move import Move
from kappa.core.geom import Vector
from . import init_property


class MoveAction:
    @staticmethod
    def init(obj: GameObject):
        init_property(obj, 'x_move', Move.NO)
        init_property(obj, 'y_move', Move.NO)

    @staticmethod
    def update_move(obj: GameObject):
        vector = Vector(0.0, 0.0, 0.0)
        direction = obj.x_move + obj.y_move

        if direction != Move.NO:
            needs_normalize = True
            if obj.x_move == Move.LEFT:
                vector[0] = -1.0
            elif obj.x_move == Move.RIGHT:
                vector[0] = 1.0
            else:
                needs_normalize = False

            if obj.y_move == Move.UP:
                vector[1] = -1.0
            elif obj.y_move == Move.DOWN:
                vector[1] = 1.0
            else:
                needs_normalize = False

            if needs_normalize:
                vector = vector.normalize()
            direction = obj.x_move + obj.y_move

            obj.move_textures[Move.NO] = obj.move_textures[direction][0]

        obj.move_vector_normalized = vector
        obj.textures = obj.move_textures[direction]
        obj.reset()
