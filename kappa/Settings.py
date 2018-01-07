import os
from datetime import datetime

import logging

PACKAGE_PARENT = 'src'
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__), os.pardir, os.pardir, os.pardir)))

LOG_DIR: str = os.path.join(SCRIPT_DIR, 'logs')
# LOG_FILE: str = 'log%s.log' % datetime.now().strftime('%Y_%m_%d_%H-%M-%S')
LOG_FILE: str = 'log.log'
LOG_LEVEL = logging.DEBUG

DRAW_DEBUG: bool = False

NEAR_OBJECTS_DRAW = 1
NEAR_OBJECTS_MOVE = 1

MAP_WIDTH = 512
MAP_HEIGHT = 512
BOX_WIDTH = 64
BOX_HEIGHT = 64
BACKGROUND_TEXTURE_WIDTH = 64
BACKGROUND_TEXTURE_HEIGHT = 64
BACKGROUND_TEXTURE_SOURCE_WIDTH = 16
BACKGROUND_TEXTURE_SOURCE_HEIGHT = 16
BOX_TEXTURE_WIDTH = BOX_WIDTH // BACKGROUND_TEXTURE_WIDTH
BOX_TEXTURE_HEIGHT = BOX_HEIGHT // BACKGROUND_TEXTURE_HEIGHT
SCREEN_DEFAULT_WIDTH = 1024
SCREEN_DEFAULT_HEIGHT = 512
CAMERA_SCREEN_POSITION_X = 0
CAMERA_SCREEN_POSITION_Y = 0
CAMERA_DEFAULT_SPEED = 1
BACKGROUND_DEFAULT_COLOR = (0, 0, 0)
