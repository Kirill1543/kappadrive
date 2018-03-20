from kappa.common.object.GameObject import GameObject
from kappa.common.object.Direction import Direction
from kappa.core.geom import Vector
from . import init_property


class MoveAction:
    @staticmethod
    def init(obj: GameObject):
        init_property(obj, 'x_move', Direction.NO)
        init_property(obj, 'y_move', Direction.NO)

    @staticmethod
    def update_move(obj: GameObject):
        vector = Vector(0.0, 0.0, 0.0)
        direction = obj.x_move + obj.y_move

        if direction != Direction.NO:
            needs_normalize = True
            if obj.x_move == Direction.LEFT:
                vector[0] = -1.0
            elif obj.x_move == Direction.RIGHT:
                vector[0] = 1.0
            else:
                needs_normalize = False

            if obj.y_move == Direction.UP:
                vector[1] = -1.0
            elif obj.y_move == Direction.DOWN:
                vector[1] = 1.0
            else:
                needs_normalize = False

            if needs_normalize:
                vector = vector.normalize()
            direction = obj.x_move + obj.y_move

            obj.move_textures[Direction.NO] = obj.move_textures[direction][0]

        obj.move_vector_normalized = vector
        obj.textures = obj.move_textures[direction]
        obj.reset()
