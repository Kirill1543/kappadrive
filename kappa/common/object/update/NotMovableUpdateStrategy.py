from kappa.common.object.update.UpdateStrategy import UpdateStrategy


class NotMovableUpdateStrategy(UpdateStrategy):
    def __init__(self, texture, update_ticks=9):
        super().__init__(texture,
                         update_ticks=update_ticks)
