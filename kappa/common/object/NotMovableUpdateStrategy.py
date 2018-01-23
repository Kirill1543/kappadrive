from ...common.object.UpdateStrategy import UpdateStrategy


class NotMovableUpdateStrategy(UpdateStrategy):
    def __init__(self, texture):
        super().__init__(texture)
