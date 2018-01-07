import pygame

from ...core.frame.Frame import Frame
from ...core.geom.Point import Point
from ...logger.Logger import Logger
from ..camera.Camera import Camera
from ..map.BoxedMap import BoxedMap
from ...Settings import NEAR_OBJECTS_DRAW, SCREEN_DEFAULT_WIDTH, SCREEN_DEFAULT_HEIGHT, BACKGROUND_DEFAULT_COLOR, \
    BACKGROUND_TEXTURE_WIDTH, BACKGROUND_TEXTURE_HEIGHT, BACKGROUND_TEXTURE_SOURCE_WIDTH, \
    BACKGROUND_TEXTURE_SOURCE_HEIGHT, BOX_WIDTH, BOX_HEIGHT, CAMERA_SCREEN_POSITION_Y, CAMERA_SCREEN_POSITION_X, \
    DRAW_DEBUG


class Screen(object):
    log = Logger(__name__).get()

    def __init__(self, w=SCREEN_DEFAULT_WIDTH, h=SCREEN_DEFAULT_HEIGHT):
        self.screen = Frame.set_mode((w, h))
        self.background = Frame.by_surface(pygame.Surface(self.screen.get_size()).convert())
        self.set_background_color(BACKGROUND_DEFAULT_COLOR)
        self.background_textures = []

        self.camera: Camera = Camera()
        self.map: BoxedMap = None
        self.blit_objects_queue: list = None

    def set_background_color(self, color_rgb):
        self.background.fill(color_rgb)

    def load_random_map(self, w, h, l=1):
        self.map = BoxedMap(w, h, l)

        self.map.set_random_background()

    def display(self):
        Screen.log.debug("Displaying background...")
        self.screen.display(self.background, (0, 0))
        Screen.log.debug("Displaying map...")
        self.screen.display(self.map.display(self.camera), (0, 0))

    def update(self):
        self.map.update()
