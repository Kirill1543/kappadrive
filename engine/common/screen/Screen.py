import pygame
import os
from engine.common.camera.Camera import Camera
from engine.common.map.Map import Map
from engine.Settings import Settings
from engine.common.object.RectObject import RectObject
from engine.common.object.CircularObject import CircularObject
from engine.common.texture.BackgroundTexture import BackgroundTexture


class Screen(object):
    def __init__(self, w=Settings.SCREEN_DEFAULT_WIDTH, h=Settings.SCREEN_DEFAULT_HEIGHT):

        print("Screen created")

        self.mode = u'MENU'
        self.screen = pygame.display.set_mode((w, h))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.set_background_color(Settings.BACKGROUND_DEFAULT_COLOR)
        self.background_textures = []

        self.camera = None
        self.map = None
        self.blit_objects_queue = None

    def load_textures(self, fullname, w=Settings.BACKGROUND_TEXTURE_WIDTH, h=Settings.BACKGROUND_TEXTURE_HEIGHT):
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        # print image.get_rect().top, image.get_rect().left, image.get_rect().w, image.get_rect().h
        s_w = Settings.BACKGROUND_TEXTURE_SOURCE_WIDTH
        s_h = Settings.BACKGROUND_TEXTURE_SOURCE_HEIGHT
        for j in range(0, 1):
            for i in range(0, 2):
                # print i, j
                self.background_textures.append(pygame.Surface((w, h)))
                self.background_textures[i].blit(
                    pygame.transform.scale(image.subsurface(i * s_w, j * s_h, s_w, s_h), (w, h)), (0, 0))

    def set_background_color(self, color_rgb):
        self.background.fill(color_rgb)

    def load_random_map(self, w, h, l=1):
        self.mode = u'MAP'
        self.map = Map(w, h, l)
        self.camera = Camera()

        self.map.set_random_background()
        # print self.map.boxes[0]

    def blit(self):
        # print "Blitting"
        self.screen.blit(self.background, (0, 0))
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

        offset_h = max(self.camera.y, 0) % Settings.BOX_HEIGHT
        pos_y = Settings.CAMERA_SCREEN_POSITION_Y - min(self.camera.y, 0)
        for box_h in range(lt_box_id[1], rb_box_id[1] + 1):
            pos_x = Settings.CAMERA_SCREEN_POSITION_X - min(self.camera.x, 0)
            offset_w = max(self.camera.x, 0) % Settings.BOX_WIDTH

            for box_w in range(lt_box_id[0], rb_box_id[0] + 1):
                img_lt_corner = (offset_w, offset_h)
                img_size = (Settings.BOX_WIDTH - offset_w, Settings.BOX_HEIGHT - offset_h)
                curr_box = self.map.boxes[self.camera.level][box_h][box_w]
                img_to_blit = curr_box.get_img(self.background_textures)
                self.screen.blit(img_to_blit.subsurface(img_lt_corner, img_size), (pos_x, pos_y))

                self.blit_objects_queue += curr_box.object_list

                pos_x += Settings.BOX_WIDTH - offset_w
                offset_w = 0

            pos_y += Settings.BOX_HEIGHT - offset_h
            offset_h = 0

    def blit_objects(self):
        for obj in self.blit_objects_queue:
            if isinstance(obj, RectObject):
                pass
            elif isinstance(obj, CircularObject):
                pygame.draw.circle(self.screen, pygame.Color(255, 0, 0),
                                   (int(obj.center.x - self.camera.x), int(obj.center.y - self.camera.y)), obj.r, 0)

    def blit_map(self):
        self.blit_objects_queue = []

        self.blit_background()
        self.blit_objects()

        self.blit_objects_queue = None

    # TO DELETE METHOD - OLD VERSION
    def blit_map_old(self):
        #
        # print "Blitting Map"
        lt_box_id = (
            max(self.camera.x // Settings.BACKGROUND_TEXTURE_WIDTH, 0),
            max(self.camera.y // Settings.BACKGROUND_TEXTURE_HEIGHT, 0)
        )
        rb_box_id = (
            min(self.camera.x + Settings.CAMERA_DEFAULT_WIDTH - 1,
                self.map.width - 1) // Settings.BACKGROUND_TEXTURE_WIDTH,
            min(self.camera.y + Settings.CAMERA_DEFAULT_HEIGHT - 1,
                self.map.height - 1) // Settings.BACKGROUND_TEXTURE_HEIGHT
        )
        offset_w = 0
        offset_h = 0
        if self.camera.x > 0:
            offset_w = self.camera.x - Settings.BACKGROUND_TEXTURE_WIDTH * lt_box_id[0]
        if self.camera.y > 0:
            offset_h = self.camera.y - Settings.BACKGROUND_TEXTURE_HEIGHT * lt_box_id[1]
        text_in_box_w = Settings.BOX_WIDTH // Settings.BACKGROUND_TEXTURE_WIDTH
        text_in_box_h = Settings.BOX_HEIGHT // Settings.BACKGROUND_TEXTURE_HEIGHT
        # print lt_box_id, rb_box_id, offset_w, offset_h
        pos_y = Settings.CAMERA_SCREEN_POSITION_Y
        is_first_h = 1
        for box_h in range(lt_box_id[1], rb_box_id[1] + 1):
            is_first_w = 1
            pos_x = Settings.CAMERA_SCREEN_POSITION_X
            for box_w in range(lt_box_id[0], rb_box_id[0] + 1):
                selected_box = self.map.boxes[self.camera.level][box_h // text_in_box_h][box_w // text_in_box_w]
                texture_id = selected_box.background[box_w % text_in_box_w][box_h % text_in_box_h]
                texture_lt = (offset_w * is_first_w, offset_h * is_first_h,)
                texture_width = Settings.BACKGROUND_TEXTURE_WIDTH - texture_lt[0]
                texture_height = Settings.BACKGROUND_TEXTURE_HEIGHT - texture_lt[1]
                texture_to_render = self.background_textures[texture_id].subsurface(texture_lt,
                                                                                    (texture_width, texture_height))

                self.screen.blit(texture_to_render, (pos_x - min(self.camera.x, 0), pos_y - min(self.camera.y, 0)))
                pos_x += Settings.BACKGROUND_TEXTURE_WIDTH
                if is_first_w:
                    pos_x -= offset_w
                    is_first_w = 0
            pos_y += Settings.BACKGROUND_TEXTURE_HEIGHT
            if is_first_h:
                pos_y -= offset_h
                is_first_h = 0
