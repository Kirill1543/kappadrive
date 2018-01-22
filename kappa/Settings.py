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
