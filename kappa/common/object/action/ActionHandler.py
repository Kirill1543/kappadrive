from kappa.common.object.GameObject import GameObject
from kappa.common.object.action.Action import Action
from kappa.common.object.action.ActionStatus import ActionStatus
from kappa.system.meta.Singleton import Singleton


class ActionHandler(metaclass=Singleton):
    def __init__(self):
        self.obj = None

    def handle(self, obj: GameObject, action: Action, **kwargs):
        self.obj = obj
        self.run_action(action, **kwargs)

    def on_success(self):
        pass

    def run_action(self, action, **kwargs):
        if action.execute(self.obj, **kwargs) == ActionStatus.SUCCESS:
            self.on_success()
