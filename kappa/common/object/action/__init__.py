from kappa.common.object.GameObject import GameObject


def init_property(obj: GameObject, prop: str, init_value):
    if not hasattr(obj, prop):
        setattr(obj, prop, init_value)
