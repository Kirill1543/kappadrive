import logging

from ..Settings import *


class Logger:
    def __init__(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(LOG_LEVEL)
        if not logger.handlers:
            file_name = os.path.join(LOG_DIR, LOG_FILE)
            handler = logging.FileHandler(file_name)
            formatter = logging.Formatter('%(asctime)s %(levelname)s:[%(name)s] %(message)s')
            handler.setFormatter(formatter)
            handler.setLevel(LOG_LEVEL)
            logger.addHandler(handler)
        self._logger = logger

    def get(self):
        return self._logger
