from ..frame.Frame import Frame

class LoadImage:
    @staticmethod
    def load_image(full_path):
        return pygame.image.load(full_path)

    @staticmethod
    def empty_image(w, h):
        return pygame.Surface(w, h)

    @staticmethod
    def scale_to(image, size):
        pygame.transform.scale(image, size)

    @staticmethod
    def crop(image, x, y, w, h):
        return image.subsurface(x, y, w, h)

    @staticmethod
    def copy_from(image, x, y, w, h, w_fin=None, h_fin=None):
        w_fin = w_fin or w
        h_fin = h_fin or h
        return LoadImage.empty_image(w_fin, h_fin).blit(
            LoadImage.scale_to(LoadImage.crop(image, x, y, w, h), (w_fin, h_fin)), (0, 0))

    @staticmethod
    def load_packed(full_path, width, height, source_width, source_height):
        image = LoadImage.load_image(full_path)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        # print image.get_rect().top, image.get_rect().left, image.get_rect().w, image.get_rect().h

        loaded_images = []

        count_width = image.get_rect().width // source_width
        count_height = image.get_rect().heght // source_height

        for j in range(0, count_height):
            for i in range(0, count_width):
                # print i, j
                loaded_images.append(LoadImage.copy_from(image, i * source_width, j * source_height, source_width, source_height, width, height))

        return loaded_images
