from ...Settings import Settings
from ...core.load.LoadImage import LoadImage


class TextureBank:
    def __init__(self):
        pass

    @staticmethod
    def load_packed(full_path, w=Settings.BACKGROUND_TEXTURE_WIDTH, h=Settings.BACKGROUND_TEXTURE_HEIGHT):
        image = LoadImage.load_image(full_path)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        # print image.get_rect().top, image.get_rect().left, image.get_rect().w, image.get_rect().h
        s_w = Settings.BACKGROUND_TEXTURE_SOURCE_WIDTH
        s_h = Settings.BACKGROUND_TEXTURE_SOURCE_HEIGHT

        loaded_textures = []

        for j in range(0, 1):
            for i in range(0, 2):
                # print i, j
                loaded_textures.append(LoadImage.copy_from(image, i * s_w, j * s_h, s_w, s_h, w, h))

        return loaded_textures
