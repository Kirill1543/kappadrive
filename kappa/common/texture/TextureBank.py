from ...core.image.Image import Image


class TextureBank:
    def __init__(self):
        self._bank = {}

    def get(self, key):
        return self._bank[key]

    def add(self, key, value):
        self._bank[key] = value

    def remove(self, key):
        del self._bank[key]

    def load_packed(self, keys, full_path, width, height, source_width, source_height):
        images = Image.load_packed(full_path, width, height, source_width, source_height)
        for i in range(len(keys)):
            self.add(keys[i], images[i])
