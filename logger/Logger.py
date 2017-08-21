import logging

from ..Settings import *


class Logger:
    def __init__(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(LOG_LEVEL)
        if not logger.handlers:
            file_name = os.path.join(LOG_DIR, LOG_FILE)
            handler = logging.FileHandler(file_name, 'w')
            handler.setLevel(LOG_LEVEL)
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s %(levelname)s:[%(name)s] %(message)s')
            handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.addHandler(console_handler)
        self._logger = logger

    def get(self):
        return self._logger
