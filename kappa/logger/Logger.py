import logging

import os

from kappa.Settings import LOG_LEVEL, LOG_DIR, LOG_FILE


class Logger:
    def __init__(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(LOG_LEVEL)
        self.log_dir = LOG_DIR
        self.check_folder_exists()
        if not logger.handlers:
            file_name = os.path.join(self.log_dir, LOG_FILE)
            handler = logging.FileHandler(file_name, 'w')
            handler.setLevel(LOG_LEVEL)
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s %(levelname)s:[%(name)s] %(message)s')
            handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.addHandler(console_handler)
        self.__logger = logger

    def get(self):
        return self.__logger

    def check_folder_exists(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
