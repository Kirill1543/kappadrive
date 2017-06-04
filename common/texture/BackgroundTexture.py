from .Texture import Texture
from ...Settings import Settings


class BackgroundTexture(Texture):
    def __init__(self):
        Texture.__init__(self, (Settings.BACKGROUND_TEXTURE_WIDTH, Settings.BACKGROUND_TEXTURE_HEIGHT))
