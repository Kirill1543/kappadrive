from engine.common.texture.Texture import Texture
from engine.Settings import Settings


class BackgroundTexture(Texture):
    def __init__(self, img=None):
        Texture.__init__(self, Settings.BACKGROUND_TEXTURE_WIDTH, Settings.BACKGROUND_TEXTURE_HEIGHT, img)
