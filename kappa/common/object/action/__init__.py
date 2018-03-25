def init_property(obj, prop: str, init_value):
    if not hasattr(obj, prop):
        setattr(obj, prop, init_value)
