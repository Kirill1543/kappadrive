import pygame

from kappa.core.frame.Frame import Frame
from kappa.core.geom.Point import Point
from kappa.logger.Logger import Logger
from ..camera.Camera import Camera
from ..map.BoxedMap import BoxedMap
from ...Settings import Settings, NEAR_OBJECTS_DRAW


class Screen(object):
    log = Logger(__name__).get()

    def __init__(self, w=Settings.SCREEN_DEFAULT_WIDTH, h=Settings.SCREEN_DEFAULT_HEIGHT):
        self.mode = u'MENU'
        self.screen = Frame.set_mode((w, h))
        self.background = Frame.by_surface(pygame.Surface(self.screen.get_size()).convert())
        self.set_background_color(Settings.BACKGROUND_DEFAULT_COLOR)
        self.background_textures = []

        self.camera: Camera = None
        self.map: BoxedMap = None
        self.blit_objects_queue: list = None

    def load_textures(self, fullname, w=Settings.BACKGROUND_TEXTURE_WIDTH, h=Settings.BACKGROUND_TEXTURE_HEIGHT):
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        s_w = Settings.BACKGROUND_TEXTURE_SOURCE_WIDTH
        s_h = Settings.BACKGROUND_TEXTURE_SOURCE_HEIGHT
        for j in range(0, 1):
            for i in range(0, 2):
                # print i, j
                self.background_textures.append(Frame.by_surface(pygame.Surface((w, h))))
                self.background_textures[i].display(
                    Frame.by_surface(pygame.transform.scale(image.subsurface(i * s_w, j * s_h, s_w, s_h), (w, h))),
                    (0, 0))

    def set_background_color(self, color_rgb):
        self.background.fill(color_rgb)

    def load_random_map(self, w, h, l=1):
        self.mode = u'MAP'
        self.map = BoxedMap(w, h, l)
        self.camera = Camera()

        self.map.set_random_background()

    def display(self):
        self.screen.display(self.background, (0, 0))
        Screen.log.debug("Camera LeftTop Position:{}".format((self.camera.x, self.camera.y)))
        if self.mode == u'MENU':
            self.blit_menu()
        elif self.mode == u'MAP':
            self.blit_map()

    @staticmethod
    def get_box_id_by_coords(x, y, w=Settings.BOX_WIDTH, h=Settings.BOX_HEIGHT):
        return x // w, y // h

    def get_box(self, x, y, l=0):
        return self.map.boxes[l][y][x]

    def get_boxes_by_camera(self):
        return (self.get_box_id_by_coords(max(int(self.camera.x), 0), max(int(self.camera.y), 0))), (
            self.get_box_id_by_coords(min(int(self.camera.x) + self.camera.width, self.map.width) - 1,
                                      min(int(self.camera.y) + self.camera.height, self.map.height) - 1))

    def blit_menu(self):
        pass

    def blit_background(self):
        lt_box_id, rb_box_id = self.get_boxes_by_camera()
        Screen.log.debug("Selected draw boxes:{}-{}".format(lt_box_id, rb_box_id))
        offset_h = max(int(self.camera.y), 0) % Settings.BOX_HEIGHT
        pos_y = Settings.CAMERA_SCREEN_POSITION_Y - min(self.camera.y, 0)
        for box_h in range(lt_box_id[1], rb_box_id[1] + 1):
            pos_x = Settings.CAMERA_SCREEN_POSITION_X - min(self.camera.x, 0)
            offset_w = max(int(self.camera.x), 0) % Settings.BOX_WIDTH

            for box_w in range(lt_box_id[0], rb_box_id[0] + 1):
                img_lt_corner = (offset_w, offset_h)
                img_size = (Settings.BOX_WIDTH - offset_w, Settings.BOX_HEIGHT - offset_h)
                curr_box = self.map.boxes[self.camera.center.z][box_h][box_w]
                img_to_blit = curr_box.build_background(self.background_textures)
                self.screen.display(img_to_blit.subframe(*img_lt_corner, *img_size), (pos_x, pos_y))

                pos_x += Settings.BOX_WIDTH - offset_w
                offset_w = 0

            pos_y += Settings.BOX_HEIGHT - offset_h
            offset_h = 0

        for box_h in range(min(lt_box_id[1] - NEAR_OBJECTS_DRAW, 0),
                           max(rb_box_id[1] + NEAR_OBJECTS_DRAW, self.map.box_height)):
            for box_w in range(min(lt_box_id[0] - NEAR_OBJECTS_DRAW, 0),
                               max(rb_box_id[0] + NEAR_OBJECTS_DRAW, self.map.box_width)):
                self.blit_objects_queue += self.map.boxes[self.camera.center.z][box_h][box_w].object_list

    def blit_objects(self):
        Screen.log.debug("BoxedMap objects list:{}".format(self.map))
        for obj in self.blit_objects_queue:
            slicing = self.camera.topleft - Point(0, 0, 0)
            obj.draw_shape_on(self.screen, obj.center - slicing)
            if obj.is_movable:
                self.map.draw_lines(self.screen, obj, slicing)

    def blit_map(self):
        self.blit_objects_queue = []

        self.blit_background()
        self.blit_objects()

        self.blit_objects_queue = None
