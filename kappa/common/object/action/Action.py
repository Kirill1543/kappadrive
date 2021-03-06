from kappa.system.meta.Singleton import Singleton


class Action(metaclass=Singleton):
    def __init__(self):
        pass

    def __str__(self):
        return "Action {}".format(self.name)

    def __repr__(self):
        return self.__str__()

    def execute(self, *args, **kwargs):
        pass

    def has_type(self, action: __name__) -> bool:
        return self.name == action.name

    def accept(self, *actions) -> bool:
        for action in actions:
            if self.has_type(action):
                return True
        return False

    @property
    def name(self):
        return None
